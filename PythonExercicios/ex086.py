matriz = list()
prov = list()
for c in range(0,3):
    for p in range(0,3):
        valor = int(input(f'Digite um valor para {c, p}: '))
        prov.append(valor)
    matriz.append(prov[:])
    prov.clear()
for c in range(0,3):
    for p in range(0,3):
        print(f'[{matriz[c][p]:^5}]', end= '')
    print()
