# 7. Faça um programa que leia um número indeterminado de valores numéricos, encerrando
# a entrada de dados quando for informado um valor igual a -1 (que não deve ser
# armazenado). Após esta entrada de dados, faça:
# Mostre a quantidade de valores que foram lidos;
# Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# Exiba todos os valores na ordem inversa à que foram informados, um ao lado do outro;
# Calcule e mostre a soma dos valores;
# Calcule e mostre a média dos valores;
# Calcule e mostre a quantidade de valores acima da média calculada

def processar_valores():

    valores = []
    print("Digite valores numéricos que deseja (digite -1 para parar):")

    while True:
        try:
            entrada = float(input())
            if entrada == -1:
                break
            valores.append(entrada)
        except ValueError:
            print("Entrada inválida. Por favor, digite um número e apenas numeros.")

    if not valores:
        print("Nenhum valor foi inserido.")
        return

    quantidade = len(valores)
    soma = sum(valores)
    media = soma / quantidade
    acima_da_media = sum(1 for valor in valores if valor > media)
    
    print("Resultados")
    print(f"1. Quantidade de valores inseridos: {quantidade}")
    
    print("2. Valores na ordem que foi digitada:", end=" ")
    print(*valores, sep=", ")
    
    print("3. Valores em ordem inversa:", end=" ")
    print(*reversed(valores), sep=", ")
    
    print(f"4. Soma de tdos valores: {soma}")
    print(f"5. Média dos valores: {media:.2f}")
    print(f"6. Quantidade dos valores que são superiores a media: {acima_da_media}")55

processar_valores()
