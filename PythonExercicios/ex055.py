pesado = 0
leve = 1000
for c in range(1,6):
    peso = float(input('Peso da {}ª pessoa: '.format(c)))
    if c == 1:
        pesado = peso
        leve = peso
    else:
        if peso >= pesado:
            pesado = peso
        if peso <= leve:
            leve = peso
print('O maior peso lido foi {}kg'.format(pesado))
print('O menor peso lido foi {}kg'.format(leve))
