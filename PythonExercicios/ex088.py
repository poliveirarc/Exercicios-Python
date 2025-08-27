from random import randint
from time import sleep
lista = list()
print('-'*30)
print(f'{'JOGA NA MEGA SENA':^30}')
print('-'*30)
num = int(input('Quantos jogos você quer que eu sorteie? '))
print('-'*30)
print(f'SORTEANDO {num} JOGOS')
for c in range(0,num):
    for p in range(0,6):
        valor = randint(1,60)
        while valor in lista:
            valor = randint(1, 60)
        if valor not in lista:
            lista.append(valor)
    lista.sort()
    print(f'Jogo {c+1}: {lista}')
    lista.clear()
    sleep(1)
print(f'{'BOA SORTE!!':^30}')