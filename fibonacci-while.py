#Sequencia de Fibonacci

print("=-" * 12)
print("Sequencia de Fibonacci")
print("=-" * 12)
num = int(input("Quantos termos voce quer mostrar: "))
t1 = 0
t2 = 1
print("=-" * 30)
print(f"{t1} > {t2}", end="")
t3 = t1 + t2
print(f" > {t3}", end="")
cont = 3
while cont <= num:
    t3 = t1 +t2
    print(f" > {t3}", end="")
    t1 = t2
    t2 = t3
    cont += 1
print(" > FIM!")
