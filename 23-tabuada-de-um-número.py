# Nome: Rafaella Ferreira Monteiro
# Exibe a tabuada de um número fornecido pelo usuário.

# Solicita ao usuário um número
numero = int(input("Digite um número para ver sua tabuada: "))

# Imprime a tabuada do número fornecido
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")