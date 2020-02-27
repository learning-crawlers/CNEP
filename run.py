# -*- coding: utf-8 -*-
import os
import csv
import json
from uuid import uuid4
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor,as_completed

def get_time_now():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

ROOT_DIR = os.path.realpath(os.path.dirname(__file__))

#===============================================================================
if __name__ == '__main__':
    print(f"{get_time_now()} Starting... ")

    fields = [ 
        'linkDetalhamento', 'cpfCnpj', 'nome', 'ufSancionado', 'orgao', 
        'razaoSocial', 'nomeFantasia', 'tipoSancao', 'dataInicialSancao', 
        'dataFinalSancao', 'valorMulta' ]

    joined = ','.join(fields)

    URL = 'http://www.portaldatransparencia.gov.br/sancoes/cnep/baixar?'
    URL = f'{URL}paginacaoSimples=true&'
    URL = f'{URL}direcaoOrdenacao=asc&'
    URL = f'{URL}colunasSelecionadas={joined}'

    CSV_FILE = 'cnep.csv'

    ROOT_CSV_PATH = os.path.join(ROOT_DIR, CSV_FILE)

    with requests.get(URL) as r:
        with open(ROOT_CSV_PATH, 'wb') as f:
            f.write(r.content)
            f.close()
            print(f"{get_time_now()} download Ok {CSV_FILE}")

    print(ROOT_CSV_PATH)

    with open(ROOT_CSV_PATH, encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        first = True

        for row in reader:
            if not first:
                cpfCnpj = row[0]
                nome = row[1]
                ufSancionado = row[2]
                orgao = row[3]
                razaoSocial = row[4]
                nomeFantasia = row[5]
                tipoSancao = row[6]
                dataInicialSancao = row[7]
                dataFinalSancao = row[8]
                valorMulta = row[9].strip()

                dict_data = { 
                    'cpfCnpj': cpfCnpj, 
                    'nome': nome, 
                    'ufSancionado': ufSancionado, 
                    'orgao': orgao, 
                    'razaoSocial': razaoSocial, 
                    'nomeFantasia': nomeFantasia, 
                    'tipoSancao': tipoSancao, 
                    'dataInicialSancao': dataInicialSancao, 
                    'dataFinalSancao': dataFinalSancao, 
                    'valorMulta': valorMulta
                }
                
                # hashing json file name with uuid
                hash = uuid4().hex

                file_json = os.path.join(ROOT_DIR, 'data', f'{hash}.json')

                # save file 
                with open(file_json, mode="w", encoding='utf8') as f:
                    f.write(json.dumps(dict_data, indent=4, ensure_ascii=False))

                print(f'{get_time_now()} [ Ok ] {hash} {nome}')

            else:
                first = not first

    exit(0)