#Um programa que leia 4 valores e guarde-os em uma tupla
#Mostrar quantas vezes apareceu valor 9
#Em que posicao foi digitado o valor 3
#Quais foram os numeros pares

num = (int(input('Digite o primeiro numero: ')), int(input('Digite o segundo numero: ')),
       int(input('Digite o terceiro numero: ')), int(input('Digite o quarto numero: ')))
print(f'Voce digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor tres apareceu primeiro na posicao {num.index(3)+1}')
else:
    print('O valor 3 nao foi digitado em nenuma posicao')
print(f'Os valores pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=', ')