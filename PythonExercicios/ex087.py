matriz = list()
prov = list()
soma = soma3coluna = maior2linha = 0
for c in range(0,3):
    for p in range(0,3):
        valor = int(input(f'Digite um valor para {c, p}: '))
        prov.append(valor)
        if valor % 2 == 0:
            soma += valor
        if p == 2:
            soma3coluna += valor
        if c == 1:
            if p == 0:
                maior2linha = valor
            else:
                if valor > maior2linha:
                    maior2linha = valor
    matriz.append(prov[:])
    prov.clear()

for c in range(0,3):
    for p in range(0,3):
        print(f'[{matriz[c][p]:^5}]', end= '')
    print()


print(f'A soma de todos os valores pares é {soma}.')
print(f'A soma dos valores da terceira coluna é {soma3coluna}.')
print(f'O maior valor da segunda linha é {maior2linha}.')