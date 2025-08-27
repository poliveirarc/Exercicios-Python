lista = list()
while True:
    valor = int(input('Digite um valor: '))
    if valor in lista:
        print('Valor duplicado! Não vou adicionar')
    else:
        lista.append(valor)
        print('Valor adicionado com sucesso!')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break
lista.sort()
print(f'Você digitou os valores {lista}')

