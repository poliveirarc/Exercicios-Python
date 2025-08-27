print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
for c in range(1, 11):
    print(primeiro, '-> ', end='')
    primeiro += razao
print('Acabou!')
