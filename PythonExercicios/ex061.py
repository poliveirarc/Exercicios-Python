print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
c = 1
while c <= 10:
    print(primeiro, '-> ', end='')
    primeiro += razao
    c += 1
print('Acabou!')
