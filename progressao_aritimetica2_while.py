#progressao aritimetica usando while com mais opcoes

print("Gerador de PA")
print("=-" * 10)
primeiro = int(input("Primeiro termo: "))
razao = int(input("Qual a razao: "))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f"{termo} > ", end="")
        termo += razao
        cont += 1
    print("Pausa")
    mais = int(input("Quantos termos voce quer mostrar mais: "))
print(f"Progressao finalizado com {total} termos mostrados")