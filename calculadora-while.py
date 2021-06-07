#Esse exercicio tem como proposta um menu com varias opcoes usando while
opcao = 0
n1 = int(input('Informe o primeiro valor: '))
n2 = int(input('Informe o segundo valor: '))
while opcao != 5:
    print("""Escolha uma opção para executar:
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Informe os numeros
    [ 5 ] Sair do programa""")
    opcao = int(input(">>>> Informe sua opção: "))
    if opcao == 1:
        soma = n1 + n2
        print(f"A soma de {n1} + {n2} = {soma}")
    elif opcao == 2:
        mult = n1 * n2
        print(f"A multiplicacao de {n1} X {n2} = {mult}")
    elif opcao == 3:
        if n1 > n2:
            print (f"O maior numero digitado foi {n1}")
        elif n1 < n2:
            print(f"O maior numero digitado foi {n1}")
        elif n1 == n2:
            print("Os numeros sao iguais")
    elif opcao == 4:
        n1 = int(input("Informe o primeiro valor: "))
        n2 = int(input("Informe o segundo valor: "))
    elif opcao == 5:
        print("Finalizando...")
    print("=-" * 15)
print("Fim do programa, volte sempre! ")
