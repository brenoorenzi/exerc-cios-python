# 9. Crie um programa que solicita ao usuário a sigla de uma moeda e exibe a cotação
# do Real (BRL) em relação a essa moeda.
# Utilize a API: https://api.exchangerate-api.com/v4/latest/BRL
#Exiba uma mensagem como "O Real vale X [nome da moeda]".

import requests

def cotacao_real():

    nomes_moedas = {
        "USD": "Dólares Americanos",
        "EUR": "Euros",
        "GBP": "Libras Esterlinas",
        "JPY": "Ienes Japoneses",
        "ARS": "Pesos Argentinos"
    }
    
    sigla_moeda = input("Digite a sigla da moeda desejada (ex: USD, EUR, GBP): ").upper()
    url = "https://api.exchangerate-api.com/v4/latest/BRL"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if sigla_moeda in data['rates']:
            taxa = data['rates'][sigla_moeda]
            nome_completo = nomes_moedas.get(sigla_moeda, sigla_moeda) 

            print(f"Real (BRL) vale {taxa:.4f} {nome_completo}.")
        else:
            print(f"Erro: essa moeda não foi encontrata '{sigla_moeda}'")
            
    except requests.exceptions.RequestException as rer:
        print(f"Erro de conexão com a API: {rer}")


cotacao_real() 
