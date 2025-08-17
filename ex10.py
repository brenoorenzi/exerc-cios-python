# 10. Faça um programa para motoristas do Uber que, ao inserir o CEP do endereço do
# destino do passageiro ele retorne qual região de São Paulo aquele CEP é.
# Utilize a documentação: https://viacep.com.br/
# As zonas de São Paulo são: Norte, Sul, Leste, Oeste e Centro. Indique também quando
# o destino é fora da cidade de São Paulo.

import requests

def verificar_zona_cep():

    cep = input("Digite o CEP (apenas números): ").replace("-", "").strip()

    if not cep.isdigit() or len(cep) != 8:
        print("este cep é invalido. Digite um comm 8 digitos.")
        return
        
    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if data.get("erro"):
            print("CEP não foi encontrado.")
            return

        cidade = data.get("localidade", "")
        bairro = data.get("bairro")

        if cidade.lower() == "são paulo":
            primeiro_digito = cep[0]
            zona = ""
            if primeiro_digito == '0':
                segundo_digito = cep[1]
                if segundo_digito == '1':
                    zona = "Zona Central"
                elif segundo_digito == '2':
                    zona = "Zona Norte"
                elif segundo_digito == '3':
                    zona = "Zona Leste"
                elif segundo_digito == '4':
                    zona = "Zona Sul"
                elif segundo_digito == '5':
                    zona = "Zona Oeste"
                else: 
                    zona = "Região Metropolitana"

            elif cep.startswith('08'):
                 zona = "Zona Leste"
            else:
                zona = "Zona não identificada"
                
            print(f"\nDestino: Bairro: {bairro}, {zona} de São Paulo.")
        else:
            uf = data.get("uf", "")
            print(f"esse CEP não se encontra em sp: ele se encontra em {cidade}, {uf}.")

    except requests.exceptions.RequestException as err:
        print(f"Erro de conexão: {err}")

verificar_zona_cep()
