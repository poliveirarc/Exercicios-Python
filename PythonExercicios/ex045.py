from random import randint
from time import sleep
print('-='*20)
print('VAMOS JOGAR JOKENPO!!')
print('-='*20)
print('''Suas opções:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
maquina = randint(1,3)
opcao = ['PEDRA', 'PAPEL', 'TESOURA']
jogador = int(input('Qual a sua jogada?: '))
if jogador == 1 or jogador == 2 or jogador == 3:
    if maquina == 1 and jogador == 2:
        resultado = 'Jogador venceu!!'
    elif maquina == 1 and jogador == 3:
        resultado = 'Máquina venceu!!'
    elif maquina == 2 and jogador == 1:
        resultado = 'Máquina venceu!!'
    elif maquina == 2 and jogador == 3:
        resultado = 'Jogador venceu!!'
    elif maquina == 3 and jogador == 1:
        resultado = 'Jogador venceu!!'
    elif maquina == 3 and jogador == 2:
        resultado = 'Máquina venceu!!'
    else:
        resultado = 'Empate!!'
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')
    print('-='*20)
    print('Computador jogou {}'.format(opcao[maquina-1]))
    print('Jogador jogou {}'.format(opcao[jogador - 1]))
    print(resultado)
else:
    print('JOGADA INVÁLIDA!!')
