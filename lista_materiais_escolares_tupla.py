#Um porgrama que crie uma lista de materiais escolares usando tupla

listagem = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9,
            'Estojo', 25, 'Transferidor', 4.20, 'Compasso', 9.99,
            'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.9)

print('-' * 30)
print(f'{"LISTAGEM DE PREÇOS":^30}')
print('-' * 30)

for p in range(0, len(listagem)):
    if p % 2 == 0:
        print(f'{listagem[p]:.<20}', end='')
    else:
        print(f'R${listagem[p]:>7.2f}')
print('-' * 30)
