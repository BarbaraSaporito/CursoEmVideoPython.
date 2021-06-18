#Um programa que faça um jogo de par ou impar contra o computador

from time import sleep
from random import randint

print("=-" * 12)
print("VAMOS JOGAR PAR OU ÍMPAR")
print("=-" * 12)
jogadas = 0
vitorias = derrotas = 0
while True:
    num = int(input("Escolha um número: "))
    par_ou_impar = str(input('''Você quer par ou ímpar? 
[P] Par
[I] Ímpar: 
''')).upper().strip()[0]
    print('''O computador esta escolhendo um número...
''')
    sleep(2)
    pc = randint(0, 10)
    soma = pc + num
    print(f'''Você jogou: {num}
O computador jogou: {pc}
Total deu {soma}.''')
    if soma % 2 == 0:
        if par_ou_impar in "Pp":
            print("DEU PAR! VOCÊ VENCEU!")
            print('''Vamos jogar novamente...
''')
            vitorias += 1
        else:
            print("DEU PAR! VOCÊ PERDEU! ")
            print('''Vamos jogar novamente...
''')
            derrotas += 1
    else:
        if par_ou_impar in "Ii":
            print("DEU ÍMPAR! VOCÊ VENCEU! ")
            print('''Vamos jogar novamente...
''')
            vitorias += 1
        else:
            print("DEU ÍMPAR! VOCÊ PERDEU! ")
            print('''Vamos jogar novamente...
''')
            derrotas += 1
    jogadas += 1
    if jogadas >= 3:
        break
if vitorias > derrotas:
    print(f'''PARABENS!!!
VOCÊ VENCEU {vitorias} VEZES''')
else:
    print(F'''GAME OVER!
VOCÊ PERDEU {derrotas} VEZES''')
sleep(12)
