import math

def calcular_trigonometria(cateto_oposto, cateto_adjacente):
    hipotenusa = math.sqrt(cateto_oposto**2 + cateto_adjacente**2)
    seno = cateto_oposto / hipotenusa
    cosseno = cateto_adjacente / hipotenusa
    tangente = cateto_oposto / cateto_adjacente if cateto_adjacente != 0 else None
    return seno, cosseno, tangente, hipotenusa

# Bloco de execução principal
print("Cálculo de Seno, Cosseno e Tangente de um Triângulo Retângulo")
print("Escolha uma opção:")
print("1: Inserir catetos")
print("2: Inserir hipotenusa e um cateto")

escolha = input("Digite 1 ou 2: ")

if escolha == '1':
    cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
    cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))
    seno, cosseno, tangente, hipotenusa = calcular_trigonometria(cateto_oposto, cateto_adjacente)
    
    print(f"\nResultados:")
    print(f"Hipotenusa: {hipotenusa}")
    print(f"Seno: {seno}")
    print(f"Cosseno: {cosseno}")
    print(f"Tangente: {tangente if tangente is not None else 'Indefinido'}")

elif escolha == '2':
    hipotenusa = float(input("Digite o comprimento da hipotenusa: "))
    cateto = float(input("Digite o comprimento do cateto conhecido: "))

    if cateto >= hipotenusa:
        print("O comprimento do cateto deve ser menor que o da hipotenusa.")
    else:
        cateto_oposto = math.sqrt(hipotenusa**2 - cateto**2)
        cateto_adjacente = cateto
        
        seno, cosseno, tangente, _ = calcular_trigonometria(cateto_oposto, cateto_adjacente)
        
        print(f"\nResultados:")
        print(f"Cateto oposto: {cateto_oposto}")
        print(f"Seno: {seno}")
        print(f"Cosseno: {cosseno}")
        print(f"Tangente: {tangente if tangente is not None else 'Indefinido'}")

else:
    print("Escolha inválida!")
