from random import randint
print('-='*15)
print('Vamos jogar par ou ímpar')
print('-='*15)
vitorias = 0
while True:
    jogador = int(input('Digite um número: '))
    computador = randint(0, 10)
    parimp = str(input('Par ou ímpar: [P/I]')).upper()
    while parimp not in 'PI':
        parimp = str(input('Par ou ímpar: [P/I]')).upper()
    soma = computador + jogador
    if soma % 2 == 0:
        parimpsoma = 'P'
        resp = 'DEU PAR'
    else:
        parimpsoma = 'I'
        resp = 'DEU ÍMPAR'
    print('-'*30)
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {soma} {resp}.')
    print('-'*30)
    if parimp == parimpsoma:
        print('Você venceu!!')
        print('Vamos jogar novamente!!')
        vitorias += 1
    else:
        print('Você perdeu!!')
        print(f'GAME OVER!! Você venceu {vitorias} vezes.')
        break



