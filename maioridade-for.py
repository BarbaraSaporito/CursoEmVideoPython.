#Programa que calcula maioridade de acordo com o ano de nascimento usando for
from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(1,8):
    nasc = int(input("Em que ano a {}o pessoa nasceu: ".format(c)))
    idade = atual - nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print("Tivemos {} pessoas maiores de idade".format(maior))
print("Tivemos {} pessoas menores de idade".format(menor))
