from modulos import requisicao_lista_estacao, requisicao_serie_dias, carregamento1_listaestacoes, carregamento2_serie_dias
import pandas as pd
import sys
import pickle
import time

requisicao_lista_estacao()
requisicao_serie_dias()

listas_estacoes_json = carregamento1_listaestacoes()
serie_dias_json = carregamento2_serie_dias()


listas_estacoes_df = pd.DataFrame.from_dict(
    listas_estacoes_json, orient='columns')

serie_dias_df = pd.DataFrame.from_dict(
    serie_dias_json, orient='columns')

print(listas_estacoes_df.head())
print(serie_dias_df.head())
