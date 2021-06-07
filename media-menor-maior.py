#Um programa que receba numeros ate o usuario parar e que diga:
#A quantidade de numeros digitados, a media entre eles e o maior e menor valor digitados

resp = "S"
soma = cont = media = maior = menor = 0
while resp in 'Ss':
    num = int(input("Digite um numero: "))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input("Quer continuar?: [S/N]: ")).upper().strip()[0]
media = soma/cont
print(f'''Foram digitados {cont} numeros
A media entre eles e {media:.2f}
O maior numero digitado foi {maior}
O menor numero digitado foi {menor}''')
