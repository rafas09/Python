# Recebe o peso e a altura do úsuario
peso = float(input("Digite seu peso (em kg): "))
altura = float(input("Digite sua altura (em metros): "))

# Calcula o IMC
imc = peso / (altura ** 2)

# Exibe o valor do IMC 
print(f"Seu IMC é de {imc:.2f}.")

# Classifica o resultado do IMC
if imc < 18.5:
    print("Você está abaixo do peso normal.")
elif 18.5 <= imc < 25:
    print("Você está no peso normal.")
elif 25 <= imc < 35:
 print("Você está com sobrepeso.")
else:
  print("Você está obeso.")
    