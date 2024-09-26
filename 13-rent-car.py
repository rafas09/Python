# Solicite os dados do usuário
km_percoridos = float(input("Informe a quantidade de Km percorridos: "))
dias_aluguel = int(input("Alugou o carro por quantos dias?:"))

# Defina os Custos
preço_por_dia = 60.0
# Preco por Dia em R$
preço_por_km = 0.15
# Preco por Km em R$

# Calcula o preço total
custo_total = (dias_aluguel * preço_por_dia) + (km_percoridos * preço_por_km)

# Exibe o resultado
print(f"O preço total a paga é: R$") 
print(f"{custo_total:.2f}")