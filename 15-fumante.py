# Solicite a quantidade de cigarros fumados por dia
cigarros_por_dia = int(input("Quantos cigarros você fuma por dia? "))

# Solicite a quantidade total de cigarros fumados 
cigarros_totais = int(input("Quantos cigarros você já fumou? "))

# Calcula a quantidade total de minutos perdidos
minutos_perdidos_por_cigarro = 10
minutos_perdidos_por_totais = cigarros_totais * minutos_perdidos_por_cigarro

# Converte minutos perdidos para dias 
minutos_perdidos_por_dia = 24 * 60
# Total de minutos em um dia 
dias_perdidos = minutos_perdidos_por_totais / minutos_perdidos_por_dia

# Exibe o resultado
print(f"Você perderá aproximadamente {dias_perdidos:.2f} dias de vida.")