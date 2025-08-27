time = list()
jogador = dict()
gols = list()
while True:
    total = 0
    jogador['nome'] = str(input('Nome do jogador: '))
    npart = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
    for n in range(1, npart+1):
        gols.append(int(input(f'Quantos gols na partida {n}: ')))
    for n in range(0, len(gols)):
        total += gols[n]
    jogador['gols'] = gols[:]
    gols.clear()
    jogador['total'] = total
    time.append(jogador.copy())
    jogador.clear()
    while True:
        resp = str(input('Você quer continuar? [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
    if resp == 'N':
        break
print(time)
print('-'*50)
print(f'{'CÓD':^5}{'NOME':^20}{'GOLS':^20}{'TOTAL':^5}')
print('-'*50)
for c in range(0, len(time)):
    print(f'{c:^5}{time[c]['nome']:^20}{str(time[c]['gols']):^20}{time[c]['total']}')
print('-' * 50)
while True:
    c = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if c == 999:
        break
    elif c < 0 or c >= len(time):
        print(f'ERRO! Não existe jogador com o código {c}')
    else:
        print(f'Levantamento do jogador {time[c]['nome']}:')
        for l,m in enumerate(time[c]['gols']):
            print(f'No jogo {l+1} fez {m} gols.')
