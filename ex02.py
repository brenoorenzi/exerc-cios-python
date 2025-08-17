# 2. Faça um programa para um caixa eletrônico. O programa deverá perguntar ao usuário o
# valor do saque e depois informar quantas notas de cada valor serão fornecidas.As notas
# disponíveis serão as de 1, 5, 10, 50 e 100 reais.O valor mínimo é de 10 reais e o máximo
# de 600 reais.

def caixa_eletronico():
    print("Caixa Eletrônico")
    valor_saque = int(input("Digite o valor que deseja sacar (valor minimo de 10,00$ reais e o maximo de 600,00$: "))

    if not 10 <= valor_saque <= 600:
        print("valor indisponivel. tente outro valor")
        return

    valor = valor_saque
    notas_100 = valor // 100
    valor %= 100

    notas_50 = valor // 50
    valor %= 50

    notas_10 = valor // 10
    valor %= 10

    notas_5 = valor // 5
    valor %= 5

    notas_1 = valor // 1

    print(f"Para sacar R${valor_saque}, você receberá:")
    if notas_100 > 0:
        print(f"{notas_100} nota(s) de R$100")
    if notas_50 > 0:
        print(f"{notas_50} nota(s) de R$50")
    if notas_10 > 0:
        print(f"{notas_10} nota(s) de R$10")
    if notas_5 > 0:
        print(f"{notas_5} nota(s) de R$5")
    if notas_1 > 0:
        print(f"{notas_1} nota(s) de R$1")

caixa_eletronico()
