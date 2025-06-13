import pandas as pd, sqlite3


def salvarCsv(df : pd.DataFrame, nome_arquivo : str, separador: str, decimal : str):
  "Armazenamento dos dados obtidos através da extração em um arquivo CSV."
  df.to_csv(nome_arquivo, sep=separador, decimal=decimal)
  return

def salvarSQLite(df : pd.DataFrame, nome_banco : str, nome_tabela: str):
  """
  Criação de um banco sqlite com os dados do conjunto de dados extraido com a API.
  """
  conn = sqlite3.connect(nome_banco) 

  df.to_sql(nome_tabela, conn, if_exists='replace', index=False)

  conn.close()
  return 

"""def salvarMySQL(
    df : pd.DataFrame, senha: str,  usuario : str, host : str, banco : str, nome_tabela : str
):
  engine = create_engine(f"mysql+pymysql://{usuario}:{senha}@{host}/{banco}")
  df.to_sql(nome_tabela, con=engine, if_exists='replace', index=False)
  return"""