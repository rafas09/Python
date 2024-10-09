import math

def calcalcular_Hipotenusa(cateto_oposto, cateto_adjacente):
    return math.sqrt(cateto_oposto**2 + cateto_adjacente**2)

def calcalcular_cateto(hipotenusa, cateto):
    return math.sqrt(hipotenusa**2 - cateto**2)

# Menu principal
def exibirMenu():
    print("Cálculo do Triângulo Retângulo usando o Teorema de Pitágoras")
    print("Escolha uma opção:")
    print("1.Calcule a hipotenusa:")
    print("2.Calcule os catetos:")
    print("3.Sair")


while True:
    exibirMenu()
    escolha = input("Digite uma das opções: ")

    if escolha == '1':
        cateto_oposto = float(input("Digite o valor do cateto oposto:"))
        cateto_adjacente = float(input("Digite o valor do cateto adjacente:"))
        hipotenusa = calcalcular_Hipotenusa(cateto_oposto, cateto_adjacente)
        print(f"\nA hipotenusa é: {hipotenusa}")

    elif escolha == '2':
        hipotenusa = float(input("Digite o valor da hipotenusa:"))
        cateto = float(input("Digite o valor de um cateto:"))
        if cateto >= hipotenusa:
            print("O comprimento do cateto deve ser menor do que o da hipotenusa.")
        else:
            cateto_faltante = calcalcular_cateto(hipotenusa, cateto)
            print(f"\nO comprimento do cateto faltante é: {cateto_faltante}")
    
    elif escolha == '3':
        print("Obrigado por usar o nosso programa!")
        break
            
    else:
        print("Opção inválida...")
        
