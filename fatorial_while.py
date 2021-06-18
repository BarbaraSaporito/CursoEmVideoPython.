#Exercicio que calcula fatorial usando while
from math import factorial

num = int(input("Digite um numero para calcular o fatorial: "))
c = num
f = 1
while c > 0:
    f *= c
    c -= 1
print(f"O fatorial de {num} é {f}")
