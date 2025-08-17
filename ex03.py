# 3. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina
# ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à
# tabela abaixo:
# Média Conceito

# Entre 9.0 e 10.0         A
# Entre 7.5 e 9.0          B
# Entre 6.0 e 7.5          C
# Entre 4.0 e 6.0          D
# Entre 4.0 e zero         E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a
# mensagem "APROVADO" se o conceito for A, B ou C ou "REPROVADO" se o conceito for
# D ou E.

def calcular_media_aluno():

    try:
        nota1 = float(input("Digite a nota da ap1 "))
        nota2 = float(input("Digite a nota da ap2 "))
    except ValueError:
        print("por favor, digite apenas as notas!!!")
        return

    media = (nota1 + nota2) / 2
    conceito = ""
    status = ""

    if 9.0 <= media <= 10.0:
        conceito = "A" 
    elif 7.5 <= media < 9.0:
        conceito = "B" 
    elif 6.0 <= media < 7.5:
        conceito = "C" 
    elif 4.0 <= media < 6.0:
       conceito = "D" 
    elif 0 <= media < 4.0:
        conceito = "E" 
    else:
        print("sua nota não foi digitada corretamente. tente novamente")
        return

    if conceito in ["A", "B", "C"]:
       status = "APROVADO!!! Parabens" 
    else:
        status = "REPROVADO!!! tente novamente no proximo semestre." 

    print("--- Resultado Final ---")
    print(f"Notas: {nota1:.1f} e {nota2:.1f}")
    print(f"Média: {media:.1f}")
    print(f"Conceito: {conceito}")
    print(f"Status: {status}")

calcular_media_aluno()

