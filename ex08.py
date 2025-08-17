# 8. Faça chamada à API restcountries, que retorna informações sobre países. Você deve exibir:
# Nome do país, linguagem(s), região, subregião com a capital
# Sigla da moeda, nome e símbolo da moeda
# Países que fazem fronteira
# Permita que o usuário insira o nome do país.

import requests

def informacoes_pais():

    nome_pais = input("Digite o nome de um país (digite em ingles, ex: Brazil, Italy): ")
    url = f"https://restcountries.com/v3.1/name/{nome_pais}"

    try:
        response = requests.get(url)
        response.raise_for_status() 

        data = response.json()[0]

        nome_comum = data['name']['common']
        linguagens = ", ".join(data['languages'].values())
        regiao = data['region']
        subregiao = data['subregion']
        capital = ", ".join(data['capital'])

        codigo_moeda = list(data['currencies'].keys())[0]
        nome_moeda = data['currencies'][codigo_moeda]['name']
        simbolo_moeda = data['currencies'][codigo_moeda]['symbol']

        fronteiras = ", ".join(data.get('borders', ["Nenhuma"]))

        print(f"Informações sobre {nome_comum}" )
        print(f"Localização: {capital} (Capital), {subregiao}, {regiao}")
        print(f"Linguagens: {linguagens}")
        print(f"Moeda: {nome_moeda} ({codigo_moeda} - {simbolo_moeda})")
        print(f"Países na fronteira: {fronteiras}")

    except requests.exceptions.HTTPError as err:
        if err.response.status_code == 404:
            print(f"o país digitado não existe ou não foi encontrato '{nome_pais}' ")
        else:
            print(f"Erro HTTP: {err}")
    except requests.exceptions.RequestException as err:
        print(f"Erro de conexão: {err}")
    except (KeyError, IndexError):
        print("Erro: Não foi possível processar os dados recebidos da API.")


informacoes_pais() 
