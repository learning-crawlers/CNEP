# CNEP
Extração de dados com Requests para listar empresas do CNEP - Cadastro Nacional de Empresas Punidas

**Executado com python v3.7**

## Modo de usar

Execute o arquivo run.py:

```bash
python run.py
```

## Resultado

**Schema**

- cpfCnpj: string
- nome: string
- ufSancionado: string
- orgao: string
- razaoSocial: string
- nomeFantasia: string
- tipoSancao: string
- dataInicialSancao: string
- dataFinalSancao: string
- valorMulta: string

**Dados**

```json
{
    "cpfCnpj": "03.240.946/0001-13",
    "nome": "ISOREL LOCACAO E SERVICOS LTDA.",
    "ufSancionado": "ISOREL LOCACAO E SERVICOS LTDA.",
    "orgao": "ISOREL",
    "razaoSocial": "BA",
    "nomeFantasia": "Multa - Lei 12.846/13",
    "tipoSancao": "22/04/2019",
    "dataInicialSancao": "Sem informação",
    "dataFinalSancao": "Petróleo Brasileiro S.A.",
    "valorMulta": "3.706.339,14"
}
```