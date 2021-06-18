#Um programa que receba numeros e some usando while, ate que o usuario deseje parar apertando 999 usando break

soma = 0
cont = 0
while True:
    num = int(input(' Digite um numero (999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma dos {cont} numeros foi {soma}')