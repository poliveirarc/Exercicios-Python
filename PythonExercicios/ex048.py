soma = 0
for c in range(1, 501, 2):
        if c % 3 == 0:
            soma += c
print('A soma entre todos os número ímpares de 1 a 500 que são múltiplos de 3 é {}.'.format(soma))