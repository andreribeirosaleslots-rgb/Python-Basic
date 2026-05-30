brasileirao =('Athletico',
'Bahia',
'Botafogo',
'Bragantino',
'Chapecoense',
'Corinthians',
'Coritiba',
'Cruzeiro',
'Flamengo',
'Fluminense',
'Grêmio',
'Internacional',
'Mirassol',
'Palmeiras',
'Remo',
'Santos',
'São Paulo',
'Vasco',
'Vitória')

print('Os 5 primeiros colocados são:')
for i in range(5):
    print(f'{i+1} - {brasileirao[i]}')
print('Os 4 últimos colocados são:')
for i in range(-4, 0):
    print(f'{len(brasileirao)+i+1} - {brasileirao[i]}')
print('Os times em ordem alfabética são:')
for i in sorted(brasileirao):
    print(i)
print(f'O Chapecoense está na {brasileirao.index("Chapecoense")+1}ª posição.')