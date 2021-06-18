#Esse exercicio tem como proposta fazer um jogo de adivinhacao usando a estrutura while

from random import randint
computador = randint(0,10)
cont = 0
print('''Sou seu computador...
Acabei de pensar em um numero entre 0 e 10
Sera que voce consegue adivinhar?''')
palpite = int(input("Qual é o sue palpite? "))
while computador != palpite:
    if computador > palpite:
        palpite = int(input("Mais... Tente outra vez: "))
        cont += 1
    else:
        palpite = int(input("Menos... Tente outra vez: "))
        cont += 1
print(f"Parabéns! Voce acertou com total de {cont + 1} tentativas!")