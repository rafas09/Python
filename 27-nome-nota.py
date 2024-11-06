# Criação de uma lista para armazenar os dados dos alunos
alunos = []

# Leitura dos dados dos 5 alunos
for i in range(5):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    nota = float(input(f"Digite a nota de {nome}: "))
    alunos.append((nome, nota))

# Exibição dos dados dos alunos
print("\nDados dos alunos:")
for aluno in alunos:
    print(f"Nome: {aluno[0]}, Nota: {aluno[1]}")
