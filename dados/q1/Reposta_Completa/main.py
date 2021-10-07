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
        codigo_estacao = 'A422'

        teste2 = requests.get(
            f'https://apitempo.inmet.gov.br/estacao/diaria/{data1}/{data2}/{codigo_estacao}')
        with open(f'json/SerieDias{codigo_estacao}.json', 'wb') as dj:
            pickle.dump(teste2.json(), dj)
        print("tarefa 2 ok")

    async def tarefa3():
        data1 = "2019-07-01"
        data2 = "2019-07-14"
        codigo_estacao = 'A360'

        teste2 = requests.get(
            f'https://apitempo.inmet.gov.br/estacao/diaria/{data1}/{data2}/{codigo_estacao}')
        with open(f'json/SerieDias{codigo_estacao}.json', 'wb') as dj:
            pickle.dump(teste2.json(), dj)
        print("tarefa 3 ok")

    async def tarefa4():
        data1 = "2019-07-01"
        data2 = "2019-07-14"
        codigo_estacao = 'A657'

        teste2 = requests.get(
            f'https://apitempo.inmet.gov.br/estacao/diaria/{data1}/{data2}/{codigo_estacao}')
        with open('json/SerieDias{codigo_estacao}.json', 'wb') as dj:
            pickle.dump(teste2.json(), dj)
        print("tarefa 4 ok")

    async def tarefa5():
        data1 = "2019-07-01"
        data2 = "2019-07-14"
        codigo_estacao = 'A908'

        teste2 = requests.get(
            f'https://apitempo.inmet.gov.br/estacao/diaria/{data1}/{data2}/{codigo_estacao}')
        with open(f'json/SerieDias{codigo_estacao}.json', 'wb') as dj:
            pickle.dump(teste2.json(), dj)
        print("tarefa 5 ok")

    async def tarefa6():
        data1 = "2019-07-01"
        data2 = "2019-07-14"
        codigo_estacao = 'A756'

        teste2 = requests.get(
            f'https://apitempo.inmet.gov.br/estacao/diaria/{data1}/{data2}/{codigo_estacao}')
        with open(f'json/SerieDias{codigo_estacao}.json', 'wb') as dj:
            pickle.dump(teste2.json(), dj)
        print("tarefa 6 ok")

    async def tarefa7():
        data1 = "2019-07-01"
        data2 = "2019-07-14"
        codigo_estacao = 'A045'

        teste2 = requests.get(
            f'https://apitempo.inmet.gov.br/estacao/diaria/{data1}/{data2}/{codigo_estacao}')
        with open(f'json/SerieDias{codigo_estacao}.json', 'wb') as dj:
            pickle.dump(teste2.json(), dj)
        print("tarefa 7 ok")

    async def tarefa8():
        data1 = "2019-07-01"
        data2 = "2019-07-14"
        codigo_estacao = 'A549'

        teste2 = requests.get(
            f'https://apitempo.inmet.gov.br/estacao/diaria/{data1}/{data2}/{codigo_estacao}')
        with open(f'json/SerieDias{codigo_estacao}.json', 'wb') as dj:
            pickle.dump(teste2.json(), dj)
        print("tarefa 8 ok")

    async def tarefa9():
        data1 = "2019-07-01"
        data2 = "2019-07-14"
        codigo_estacao = 'A534'

        teste2 = requests.get(
            f'https://apitempo.inmet.gov.br/estacao/diaria/{data1}/{data2}/{codigo_estacao}')
        with open(f'json/SerieDias{codigo_estacao}.json', 'wb') as dj:
            pickle.dump(teste2.json(), dj)
        print("tarefa 9 ok")

    async def tarefa10():
        data1 = "2019-07-01"
        data2 = "2019-07-14"
        codigo_estacao = 'A617'

        teste2 = requests.get(
            f'https://apitempo.inmet.gov.br/estacao/diaria/{data1}/{data2}/{codigo_estacao}')
        with open(f'json/SerieDias{codigo_estacao}.json', 'wb') as dj:
            pickle.dump(teste2.json(), dj)
        print("tarefa 10 ok")

    async def tarefa11():
        data1 = "2019-07-01"
        data2 = "2019-07-14"
        codigo_estacao = 'A826'

        teste2 = requests.get(
            f'https://apitempo.inmet.gov.br/estacao/diaria/{data1}/{data2}/{codigo_estacao}')
        with open(f'json/SerieDias{codigo_estacao}.json', 'wb') as dj:
            pickle.dump(teste2.json(), dj)
        print("tarefa 11 ok")

    async def tarefa12():
        data1 = "2019-07-01"
        data2 = "2019-07-14"
        codigo_estacao = 'A615'

        teste2 = requests.get(
            f'https://apitempo.inmet.gov.br/estacao/diaria/{data1}/{data2}/{codigo_estacao}')
        with open(f'json/SerieDias{codigo_estacao}.json', 'wb') as dj:
            pickle.dump(teste2.json(), dj)
        print("tarefa 12 ok")

    async def tarefa13():
        data1 = "2019-07-01"
        data2 = "2019-07-14"
        codigo_estacao = 'A053'

        teste2 = requests.get(
            f'https://apitempo.inmet.gov.br/estacao/diaria/{data1}/{data2}/{codigo_estacao}')
        with open(f'json/SerieDias{codigo_estacao}.json', 'wb') as dj:
            pickle.dump(teste2.json(), dj)
        print("tarefa 13 ok")

    async def tarefa14():
        data1 = "2019-07-01"
        data2 = "2019-07-14"
        codigo_estacao = 'A508'

        teste2 = requests.get(
            f'https://apitempo.inmet.gov.br/estacao/diaria/{data1}/{data2}/{codigo_estacao}')
        with open(f'json/SerieDias{codigo_estacao}.json', 'wb') as dj:
            pickle.dump(teste2.json(), dj)
        print("tarefa 14 ok")

    async def tarefa15():
        data1 = "2019-07-01"
        data2 = "2019-07-14"
        codigo_estacao = 'A924'

        teste2 = requests.get(
            f'https://apitempo.inmet.gov.br/estacao/diaria/{data1}/{data2}/{codigo_estacao}')
        with open(f'json/SerieDias{codigo_estacao}.json', 'wb') as dj:
            pickle.dump(teste2.json(), dj)
        print("tarefa 15 ok")

    async def tarefa16():
        data1 = "2019-07-01"
        data2 = "2019-07-14"
        codigo_estacao = 'A253'

        teste2 = requests.get(
            f'https://apitempo.inmet.gov.br/estacao/diaria/{data1}/{data2}/{codigo_estacao}')
        with open(f'json/SerieDias{codigo_estacao}.json', 'wb') as dj:
            pickle.dump(teste2.json(), dj)
        print("tarefa 16 ok")

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
        tarefa_3 = asyncio.create_task(tarefa3())
        tarefa_4 = asyncio.create_task(tarefa4())
        tarefa_5 = asyncio.create_task(tarefa5())
        tarefa_6 = asyncio.create_task(tarefa6())
        tarefa_7 = asyncio.create_task(tarefa7())
        tarefa_8 = asyncio.create_task(tarefa8())
        tarefa_9 = asyncio.create_task(tarefa9())
        tarefa_10 = asyncio.create_task(tarefa10())
        tarefa_11 = asyncio.create_task(tarefa11())
        tarefa_12 = asyncio.create_task(tarefa12())
        tarefa_13 = asyncio.create_task(tarefa13())
        tarefa_14 = asyncio.create_task(tarefa14())
        tarefa_15 = asyncio.create_task(tarefa15())
        tarefa_16 = asyncio.create_task(tarefa16())

        await tarefa_1
        await tarefa_2

        tarefa_3 = asyncio.create_task(tarefa3())

    asyncio.run(main())
