pessoas = list()
dados = list()
cont = pesado = leve = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    cont += 1
    for p in pessoas:
        if cont == 1:
            pesado = leve = p[1]
        else:
            if p[1] > pesado:
                pesado = p[1]
            elif p[1] < leve:
                leve = p[1]
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Você quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break

print(f'Ao todo você cadastrou {cont} pessoas.')
print(f'O maior peso foi {pesado}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == pesado:
        print (f'[{p[0]}]', end=' ')
print(f'\nO menor peso foi {leve}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == leve:
        print (f'[{p[0]}]', end=' ')
