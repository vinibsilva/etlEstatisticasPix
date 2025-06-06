from src.extractTransform import requestApiBcb
from src.load import salvarCsv, salvarSQLite, salvarMySQL
import pandas as pd

dadosBcb = requestApiBcb('20191')
salvarCsv(dadosBcb, "./src/datasets/transacoesPixPorMunicipio.csv", ';', '.')

salvarSQLite(dadosBcb, "./src/datasets/etlbcb.db", "transacoes_Pix_Municipio")

#salvarMySQL(dadosBcb, 'teste', 'root', 'localhost', 'etlbcb', 'meios_pagamentos_tri')