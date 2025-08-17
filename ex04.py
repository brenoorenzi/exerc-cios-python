
# 4. Desenvolver um programa para verificar a nota dos alunos em uma prova com 10
# questões. O programa deve seguir os seguintes passos:
# Perguntar ao aluno a resposta de cada uma das 10 questões. 
# Comparar as respostas fornecidas pelo aluno com o gabarito da prova.
# Calcular o total de acertos, atribuindo 1 ponto para cada resposta correta. 
# Após cada aluno utilizar o sistema, perguntar se outro aluno deseja fazer a prova. 
# Após todos os alunos terem respondido, o programa deve informar:
# O maior e o menor número de acertos entre os alunos. 
# O total de alunos que utilizaram o sistema. 
# A média das notas da turma.

def sistema_prova():
    gabarito = ['A', 'C', 'B', 'A', 'E', 'D', 'D', 'B', 'A', 'E']
    notas_turma = []

    while True:
        print(" coloque as respostas do aluno: ")
        respostas_aluno = []
        acertos = 0

        for i in range(10):
            while True:
                resposta = input(f"Digite as respostas das questões {i + 1} (A, B, C, D ou E): ").upper()
                if resposta in ['A', 'B', 'C', 'D', 'E']:
                    respostas_aluno.append(resposta)
                    break
                else:
                    print("Alternativa não existe. Por favor, digite uma que seja valida")

        for i in range(10):
            if respostas_aluno[i] == gabarito[i]:
                acertos += 1
        
        notas_turma.append(acertos)
        print(f"Este aluno acertou {acertos} questões.")
        
        continuar = input("\nOutro aluno vai utilizar o sistema? (S ou N): ").upper()
        if continuar != 'S':
            break

    if notas_turma:
        maior_acerto = max(notas_turma) 
        menor_acerto = min(notas_turma) 
        total_alunos = len(notas_turma)
        media_turma = sum(notas_turma) / total_alunos 

        print("\n--- Estatísticas da Turma ---")
        print(f"Maior número de acertos: {maior_acerto}")
        print(f"Menor número de acertos: {menor_acerto}")
        print(f"Total de alunos que utilizaram o sistema: {total_alunos}")
        print(f"Média das notas da turma: {media_turma:.2f}")
    else:
        print("\nNenhum aluno utilizou o sistema.")

sistema_prova()
