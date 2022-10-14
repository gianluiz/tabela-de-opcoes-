#Este é um programa que lê dois valores e mostra um menu na tela: (utilização da Estrutura 'while')
print("""[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.""")
opcao = 4
while opcao == 4:
    while True:
        try:
            v1 = int(input("Escolha o primeiro VALOR->"))
            print(v1)
            break
        except ValueError:
            print("ERRO. Digite um Valor de Número Inteiro.")
    while True:
        try:
            v2 = int(input("Escolha o segundo VALOR->"))
            print(v2)
            break
        except ValueError:
            print("ERRO. Digite um Valor de Número Inteiro.")
    while True:
        try:
            opcao = int(input("Digite uma opção disponível:"))
            break
        except ValueError:
            print("ERRO.Digite um número, entre as opções do MENU: [1]-[2]-[3]-[4]-[5]")

            v1 = int(input("Escolha o Valor 1->"))
            print(v1)
            break
        except:
            print("ERRO. Digite um Valor de Número Inteiro.")
    while True:
        try:
            v2 = int(input("Escolha o Valor 2->"))
            print(v2)
            break
        except:
            print("ERRO. Digite um Valor de Número Inteiro.")
    opcao = int(input("Digite uma opção disponível:"))

    if opcao == 1:
        print(f"Opção SOMA -> {v1}+{v2} = {v1 + v2}")
    elif opcao == 2:
        print(f"Opção MULTIPLICAR -> {v1}X{v2} = {v1 * v2}")
    elif opcao == 3:
        if v1 > v2:
            print(f"O Valor1-> {v1} é maior que o Valor2-> {v2}")
        elif v1 < v2:
            print(f"O Valor2-> {v2} é maior que o Valor1-> {v1}")
        else:
            print("Os 2 valores são iguais.")
    elif opcao == 5:
        print("Sair do programa\nTCHAU!")
    else:
        print("Opção Indisponível.\nReinicie o Programa.As as opções do MENU são [1]-[2]-[3]-[4]-[5]")
print("\nObrigado! Volte sempre!")



