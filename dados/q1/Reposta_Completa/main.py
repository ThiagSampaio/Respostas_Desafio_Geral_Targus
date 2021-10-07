import pandas as pd
import pickle
import asyncio
import requests

if __name__ == "__main__":

    async def tarefa1():
        tipo_estacao = 'T'
        teste1 = requests.get(
            f'https://apitempo.inmet.gov.br/estacoes/{tipo_estacao}')
        with open('json/ListaEstacoes.json', 'wb') as dj:
            pickle.dump(teste1.json(), dj)
        print("tarefa 1")

    async def tarefa2():
        data1 = "2019-07-01"
        data2 = "2019-07-14"
        codigo_estacao = 'A756'

        teste2 = requests.get(
            f'https://apitempo.inmet.gov.br/estacao/diaria/{data1}/{data2}/{codigo_estacao}')
        with open('json/SerieDias.json', 'wb') as dj:
            pickle.dump(teste2.json(), dj)
        print("tarefa 2 ok")

    async def tarefa3():

        with open('json/ListaEstacoes.json', 'rb') as fp:
            listas_estacoes_json = pickle.load(fp)

        with open('json/SerieDias.json', 'rb') as fp:
            serie_dias_json = pickle.load(fp)

        listas_estacoes_df = pd.DataFrame.from_dict(
            listas_estacoes_json, orient='columns')

        serie_dias_df = pd.DataFrame.from_dict(
            serie_dias_json, orient='columns')

        print(listas_estacoes_df.head())
        print(serie_dias_df.head())

    async def main():

        tarefa_1 = asyncio.create_task(tarefa1())
        tarefa_2 = asyncio.create_task(tarefa2())

        await tarefa_1
        await tarefa_2

        tarefa_3 = asyncio.create_task(tarefa3())

    asyncio.run(main())
