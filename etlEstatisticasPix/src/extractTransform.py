import requests
import pandas as pd



def requestApiBcb(data: str) -> pd.DataFrame:
  """
  Função para extrair os dados sobre estatísticas de Transações Pix por Município.
  
  Parâmetros: 
  Data - String - aaaat (Exemplo: 202401)

  Saída:
  DataFrame - Estrutura de dados do Pandas.
  """
  url = f"https://olinda.bcb.gov.br/olinda/servico/Pix_DadosAbertos/versao/v1/odata/TransacoesPixPorMunicipio(DataBase=@DataBase)?@DataBase='{data}'&$top=10000&$format=json"

  req = requests.get(url)
  dados = req.json()

  df = pd.json_normalize(dados['value'])
  df['Data-base'] = pd.to_datetime(df['Data-base'])
  return df