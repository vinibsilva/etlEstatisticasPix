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
  url = f"https://olinda.bcb.gov.br/olinda/servico/Pix_DadosAbertos/versao/v1/odata/TransacoesPixPorMunicipio(DataBase=@DataBase)?@DataBase='{data}'&$top=5000&$format=json&$select=AnoMes,Municipio_Ibge,Municipio,Estado_Ibge,Estado,Sigla_Regiao,Regiao,VL_PagadorPF,QT_PagadorPF,VL_PagadorPJ,QT_PagadorPJ,VL_RecebedorPF,QT_RecebedorPF,VL_RecebedorPJ,QT_RecebedorPJ,QT_PES_PagadorPF,QT_PES_PagadorPJ,QT_PES_RecebedorPF,QT_PES_RecebedorPJ"

  req = requests.get(url)
  dados = req.json()

  df = pd.json_normalize(dados['value'])
  df['AnoMes'] = pd.to_datetime(df['AnoMes'])
  return df