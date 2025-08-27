lista = list()
listapar = list()
listaimp = list()
while True:
    lista.append(int(input('Digite um número: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Você quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
for c in lista:
    if c % 2 == 0:
        listapar.append(c)
    else:
        listaimp.append(c)
print(f'A lista completa é {lista}.')
print(f'A lista de pares é {listapar}.')
print(f'A lista de ímpares é {listaimp}.')