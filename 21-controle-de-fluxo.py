for num in range (1,101):
    if num == 6:
        print("não vou mostrar o 6!")
        continue # pula a exibição do 6
    elif num >= 10 and num <= 27:
        print(f"não vou mostrar o {num}!")
        continue # pula a exibição dos números de 10 até 27
    elif num == 41:
        break
    else:
        print(f"contagem {num}")
print("acabou. :)")