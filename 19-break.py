condicao = True

while condicao:
    nome =  input('Qual seu nome:')

    if nome == 'Sair':
        break # para a execução do while, sai do loop de repetição

    print(f'Seu nome é {nome}')

print('Acabou')