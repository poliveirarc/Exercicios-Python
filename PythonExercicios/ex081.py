lista = list()
while True:
    lista.append(int(input('Digite um número: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Você quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print(f'Foram digitados {len(lista)} números.')
lista.sort(reverse=True)
print(f'A lista de valores em ordem descrescente é {lista}')
if 5 in lista:
    print('O valor 5 ESTÁ na lista.')
else:
    print('O valor 5 NÃO ESTÁ na lista.')
