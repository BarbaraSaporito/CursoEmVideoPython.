# Um programa que crie estatisticas de compras motrando:
# Valor total da compra
# Quantos produtos custaram mais que 1000 reais
# Produto mais barato

print("=" * 20)
print("loja super baratão".upper())
print("=" * 20)

preco = total = produtos = menor = cont = 0
nome = barato = ""
while True:
    nome = str(input("Qual o nome do produto: "))
    preco = float(input("Qual o valor do produto: R$ "))
    cont += 1
    total += preco
    if preco > 1000:
        produtos += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome
    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Quer continuar? [S/N]: ")).upper().strip()[0]
    if continuar in "N":
        break
print(f"O total da compra foi {total:.2f}")
print(f"O total de produtos que custaram mais de 1,000 reais foi {produtos}")
print(f"O produto com menor valor é {barato} e custa R$ {menor:.2f} ")
print("FIM DO PROGRAMA!")
