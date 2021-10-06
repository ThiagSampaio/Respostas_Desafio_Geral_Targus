import json
import requests
import pickle
import sys
import os
from datetime import datetime, timedelta

# ###Bloco 1 - Criação de datas### #


def datas_requisisao(delta=14):
    '''
    Função para aquisição e tratamento de datas.

    Input: Inteiro(delta) representando o intervalo de dias para requisição. 
           Delta Default de 14 dias, como pedido na requisição do programa. 

    Output: Data de hoje e Data passada (-14 dias)
    '''

    data_hoje = datetime.today()
    delta_entre_datas = delta
    data_passado = data_hoje - timedelta(days=delta_entre_datas)

    data_hoje_requisicao = data_hoje.strftime('%Y-%m-%d')
    data_passada_requisicao = data_passado.strftime('%Y-%m-%d')

    return data_passada_requisicao, data_hoje_requisicao


# ###Bloco2 - Criação das URL´S### #


def url_requisicoes(tipo_estacao='T', codigo_estacao='A301'):
    '''
    Função para a 'fabricação' da requisição da API do INMET. 
    Ver documentação em: https://portal.inmet.gov.br/manual/manual-de-uso-da-api-esta%C3%A7%C3%B5es

    Input: Tipo da estação T ou M para primeira requisição. 
           Codigo da estacao para segunda requisição

    Output: Duas URL montadas para a requisição via API

    '''

    url_estacoes = f'https://apitempo.inmet.gov.br/estacoes/{tipo_estacao}'
    url_estacoes_dadosHorarios = f'https://apitempo.inmet.gov.br/estacao/{datas_requisisao()[0]}/{datas_requisisao()[1]}/{codigo_estacao}'

    return url_estacoes, url_estacoes_dadosHorarios


# ###Bloco3 - Requisições ### #


def requisicao_lista_estacao():
    """
    Função para requisição de lista das estações, gerando arquivo ListaEstacoes.json na pasta resposta_json
    """
    try:
        lista_estacoes = requests.get(url_requisicoes()[0])
        lista_estacoes_json = lista_estacoes.json()
        lista_estacoes.raise_for_status()
        with open('json/ListaEstacoes.json', 'wb') as dj:
            pickle.dump(lista_estacoes_json, dj)
        print("Requisição Lista de estações finalizado com Sucesso!")

    # Tratamento de erros
    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else", err)


def requisicao_serie_dias():
    """
    Função para requisição de serie de dias, gerando arquivo SerieDias.json na pasta resposta_json
    """
    try:
        serie_dias = requests.get(url_requisicoes()[1])
        serie_dias.raise_for_status()
        with open('json/SerieDias.json', 'wb') as dj:
            pickle.dump(serie_dias.json(), dj)
        print("Requisicção serie dias finalizado com Sucesso!")

    # Tratamento de erros
    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else", err)


# ###Bloco4 - Carregamento de variaveis json na main ### #


def carregamento1_listaestacoes():
    '''
    Função para o carramento do arquivo json na main.
    Não é necessária esta função, porém ela se faz util caso o usuário queira visualizar o Json

    Output: variavel com dados .json gravados.
    '''

    try:
        with open('json/ListaEstacoes.json', 'rb') as fp:
            listas_estacoes = pickle.load(fp)
            return listas_estacoes
    except FileNotFoundError:
        print('Está faltando o arquivo ListaEstacoes.json')
        sys.exit(-1)


def carregamento2_serie_dias():
    '''
    Função para o carramento do arquivo .json na main.
    Não é necessária esta função, porém ela se faz util caso o usuário queira visualizar o Json

    Output: variavel com dados .json gravados.
    '''

    try:
        with open('json/SerieDias.json', 'rb') as fp:
            serie_dias = pickle.load(fp)
            return serie_dias
    except FileNotFoundError:
        print('Está faltando o arquivo SerieDias.json')
        sys.exit(-1)

# ###Bloco5 - Transformacao de json para df ### #
