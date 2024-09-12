# Recebe o ano do úsuario
ano = int(input("Digite o ano que você deseja saber se é bissexto: "))

# Verificar se o ano e bissexto
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
 print(f"O ano {ano} é bissexto!")
else:
 print(f"O ano {ano} não é bissexto!")