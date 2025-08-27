aprov = dict()
gols = list()
total = 0
aprov['nome'] = str(input('Nome do jogador: '))
npart = int(input(f'Quantas partidas {aprov['nome']} jogou? '))
for n in range(1, npart+1):
    gols.append(int(input(f'Quanto gols na partida {n}: ')))
for n in range(0, len(gols)):
    total += gols[n]
aprov['gols'] = gols[:]
aprov['total'] = total
print('-'*30)
print(aprov)
print('-'*30)
for l, m in aprov.items():
    print(f'o campo {l} tem valor {m}')
print('-'*30)
print(f'O jogador {aprov['nome']} jogou {npart} partidas.')
for l,m in enumerate(aprov['gols']):
    print (f' => Na partida {l+1}, fez {m} gols.')