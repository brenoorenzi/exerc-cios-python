# 6. Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
# Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
# Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
# A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do
# percentual do ano anterior.
# Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere
# o programa permitindo que o usuário digite o salário inicial do funcionário.

import datetime

def calcular_salario_atual():
    try:
        salario_inicial = float(input("Digite qual era o salário em  1995: R$ "))
    except ValueError:
        print("Salário muito baixo. digite um valor maior.")
        return

    ano_contratacao = 1995
    ano_atual = datetime.datetime.now().year
    
    salario = salario_inicial
    percentual_aumento = 0.015 

    for ano in range(ano_contratacao + 1, ano_atual + 1):
        aumento = salario * percentual_aumento
        salario += aumento
        print(f"Salário em {ano}: R$ {salario:.2f} (aumento de {percentual_aumento*100:.2f}%)")
  
        percentual_aumento *= 2

    print(f"\nO salário atual ({ano_atual}) do funcionário é: R$ {salario:.2f}")

calcular_salario_atual()
