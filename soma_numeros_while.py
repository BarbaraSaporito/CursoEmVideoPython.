#Um programa que receba numeros e some usando while, ate que o usuario deseje parar apertando 999

cont = 0
soma = 0
num = 0
num = int(input("Digite um numero: (999 para sair):  "))
while num != 999:
    cont += 1
    soma += num
    num = int(input("Digite um numero: (999 para sair):  "))
print(f"A soma dos {cont} numeros digitados e de {soma}")
