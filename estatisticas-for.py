#Um programa que pega dado de 5 pessoas
#Verifica a media de idade do grupo
#Mostra o homem  mais velho e como se chama
#Mostra o total de mulheres com menos de 20 anos'''

midade = 0
sidade = 0
midadeh = 0
nomevelho = ''
totalm = 0

for p in range(1,6):
    print(' {}ª PESSOA'.format(p))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    sidade += idade
    if p == 1 and sexo in 'Mm':
        midadeh = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > midadeh:
        midadeh = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totalm += 1

midade = sidade/p
print('A media da idade do grupo e de {} anos'.format(midade))
print('O homem mais velho tem {} anos e se chama {} '.format(midadeh, nomevelho.capitalize()))
print('Ao todo sao {} mulheres com menos de 20 anos'.format(totalm))
