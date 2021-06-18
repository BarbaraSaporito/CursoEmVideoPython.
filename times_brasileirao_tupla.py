#Um programa que crie uma tupla com a lista de times do Brasileirao
#Que contenha os 20 primeiros colocados da tabela em sua ordem
#Mostrar os 5 primeiros
#Mostrar os ultimos 4 colocados
#Mostrar times em ordem alfabetica
#Mostrar a posicao do time Chapecoense

times = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
    'Atlético Mineiro', 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos',
    'Bahia', 'Corinthians', 'Fluminense', 'Ceará', 'Vasco da Gama', 'Sport Recife',
    'América-MG', 'Chapecoense', 'Vitória', 'Paraná')
print('-=' * 40)
print(f'Lista de times do Brasileirao {times}')
print('-=' * 40)
print(f'Os 5 primeiros sao {times[0:5]}')
print('-=' * 40)
print(f'Os 4 ultimos sao {times[-4:]}')
print('-=' * 40)
print(f'Os times em ordem alfabetica: {sorted(times)}')
print('-=' * 40)
print(f'A posicao do time Chapecoense e {times.index("Chapecoense")+1}º')