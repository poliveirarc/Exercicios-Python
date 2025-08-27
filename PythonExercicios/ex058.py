from random import randint
computador = randint(0,10)
tentativas = 0
print('''Sou seu computador...
Acabei de pensar num número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')
jogador = int(input('Qual é seu palpite?: '))
while jogador != computador:
    if jogador < computador:
        print('Mais... tente mais uma vez!')
        jogador = int(input('Qual é seu palpite?: '))
    else:
        print('Menos... tente mais uma vez!')
        jogador = int(input('Qual é seu palpite?: '))
    tentativas += 1
print('Acertou!! Foram necessárias {} tentativas!'.format(tentativas+1))
