from random import randint
from time import sleep
n = randint(0,5)
print('-'*50)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar ')
print('-'*50)
num = int(input('Em que número eu pensei?: '))
print('PROCESSANDO...')
sleep(3)
if num == 5:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}.'.format(n, num))