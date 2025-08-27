from random import randint
from time import sleep
from operator import itemgetter
jogadas = {'jogador1' : randint(1,6),
            'jogador2' : randint(1,6),
            'jogador3' : randint(1,6),
            'jogador4' : randint(1,6)}
print('==== JOGADAS ====')
for l,m in jogadas.items():
    print(f'{l} tirou {m}.')
    sleep(1)
print()
ranking = list()
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
print('== RANKING DOS JOGADORES ==')
for l,m in enumerate(ranking):
    print(f'{l+1}º lugar = {m[0]} com {m[1]}')
    sleep(1)

