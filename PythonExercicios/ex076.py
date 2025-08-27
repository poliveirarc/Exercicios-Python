produtos = ('Lápis', 2.99, 'Caderno', 10.50, 'Estojo', 12.90,
            'Grampeador', 35.00, 'Borracha', 0.50, 'Lapiseira', 6.90)
print('-'*40)
print(f'{'LISTAGEM DE PRODUTOS':^40}')
print('-'*40)
for c in range(0, len(produtos)):
    if c % 2 == 0:
        print(f'{produtos[c]:.<30}', end='')
    else:
        print(f'R${produtos[c]:>8.2f}')
