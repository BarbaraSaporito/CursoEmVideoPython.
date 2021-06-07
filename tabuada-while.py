#Um programa que faca tabuada do numero escolhido pelo usuario, usando o while
from time import sleep
resp = "s"
while resp in "Ss":
    num = int(input("Quer ver a tabuada de qual numero: "))
    print("-" * 30)
    for c in range(1,11):
        print(f"{num} X {c} = {num*c}")
    resp = str(input("Quer escolher outro numero? [S/N]:")).upper().strip()[0]
    print("-" * 30)
print("Encerrando o programa...")
sleep(1)
print("FIM!")