from src.extractTransform import requestApiBcb
from src.load import salvarCsv, salvarSQLite
import pandas as pd

dadosBcb = requestApiBcb('202111')
salvarCsv(dadosBcb, "./src/datasets/transacoesPixPorMunicipio.csv", ';', '.')

salvarSQLite(dadosBcb, "./src/datasets/etlbcb.db", "transacoesPixPorMunicipio")

#salvarMySQL(dadosBcb, 'teste', 'root', 'localhost', 'etlbcb', 'meios_pagamentos_tri')