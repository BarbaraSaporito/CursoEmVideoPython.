#Programa que faca a contagem de 1 ate o numero escolhido pelo usuario usando for
num = int(input('Digite um numero: '))
for c in range(1, num + 1):
    if num % 2 == 0:
        print("\033[33m", end=' ')
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
