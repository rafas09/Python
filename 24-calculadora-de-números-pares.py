# Nome: Rafaella Ferreira Monteiro
# Calcula a soma dos números pares entre 1 e 50.

soma = 0
for numero in range(1, 51):
    if numero % 2 == 0:  # Verifica se o número é par
        soma += numero

print("Soma dos números pares entre 1 e 50:", soma)