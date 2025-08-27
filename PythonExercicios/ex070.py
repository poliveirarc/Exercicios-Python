print('-'*20)
print('LOJA SUPER BARATÃO')
print('-'*20)
total = acimamil = maisbarato = cont = 0
pmaisbarato = ' '
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    resp = ' '
    total += preço
    cont += 1
    if cont == 0:
        maisbarato = preço
        pmaisbarato = produto
    if preço > 1000:
        acimamil += 1
    if preço < maisbarato:
        pmaisbarato = produto
    while resp not in 'NS':
        resp = str(input('Quer continuar: [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('============= FIM DO PROGRAMA =============')
print(f'O total da compra foi R${total:.2f}.')
print(f'Temos {acimamil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {pmaisbarato}, custando R${maisbarato:.2f}.')

