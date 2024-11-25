from pathlib import Path


PASTA_PROJETO = Path(__file__).resolve().parents[2]

PASTA_DADOS = PASTA_PROJETO / "dados"

# coloque abaixo o caminho para os arquivos de dados de seu projeto
DADOS_ORIGINAIS = PASTA_DADOS / "diabetes_binary_5050split_health_indicators_BRFSS2015.csv"
DADOS_TRATADOS = PASTA_DADOS / "diabetes_tratado.parquet"

# coloque abaixo outros caminhos que você julgar necessário
PASTA_RELATORIOS = PASTA_PROJETO / "relatorios"
PASTA_IMAGENS = PASTA_RELATORIOS / "imagens"
