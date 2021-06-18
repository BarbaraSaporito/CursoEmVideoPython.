#Um programa que some 6 valores usando a estrutura for
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print('A soma dos de {} numeros pares e {}'.format(cont, soma))
