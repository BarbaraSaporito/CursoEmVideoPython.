# Um programa que analise quantos maiores de 18 anos
# Quantos homens cadastrados
# Quantas mulheres com menos de 20 anos
from time import sleep
print("=" * 20)
print("Cadastre uma pessoa".upper())
print("=" * 20)
idade = maiores = homem = mulher = 0
while True:
    idade = int(input("Idade: "))
    if idade >= 18:
        maiores += 1
    sexo = ' '
    while sexo not in 'MmFf':
        sexo = str(input("Sexo: [F/M]: "))
    if sexo in 'Mm':
        homem += 1
    if sexo in 'Ff' and idade < 20:
        mulher += 1
    continuar = " "
    while continuar not in 'SN':
        continuar = str(input('''Quer continuar?  
[S] - SIM
[N] - NAO:
''')).upper().strip()[0]
    if continuar == 'N':
        break
sleep(2)
print(f"Total de {maiores} pessoas com mais de 18 anos ")
print(f"Ao todo temos {homem} homens cadastrados ")
print(f"E temos {mulher} mulheres com menos de 20 anos")
