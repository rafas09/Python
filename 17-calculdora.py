def calculadora():
 while True:
        print("CALCULADORA DAS OPERAÇÕES BÁSICAS:")
        print("Menu de escolha")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Resto da Divisão")
        print("6. Sair")
        opcao = int(input("Digite uma opção: "))

        if opcao == 1:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            resultado = num1 + num2
            print("Resultado da soma:", resultado, "\n")

        elif opcao == 2:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            resultado = num1 - num2
            print("Resultado da subtração:", resultado, "\n")

        elif opcao == 3:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            resultado = num1 * num2
            print("Resultado da multiplicação:", resultado, "\n")

        elif opcao == 4:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            if num2 != 0:
                resultado = num1 / num2
                print("Resultado da divisão:", resultado, "\n")
            else:
                print("Erro: Divisão por zero não é permitida.\n")

        elif opcao == 5:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            if num2 != 0:
                resultado = num1 % num2
                print("Resultado do resto da divisão:", resultado, "\n")
            else:
                print("Erro: Divisor não pode ser zero.\n")
 
        elif opcao == 6:
            print("Saindo...")
            break

        else:
            print("Opção Inválida\n")

# Chama a função da calculadora
calculadora()
