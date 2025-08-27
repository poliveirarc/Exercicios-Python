def ficha(jogador = '<desconhecido>', gols = 0):
    if gols.isnumeric() == False:
        gols = 0
    return f'O jogador {jogador} fez {gols} gol (s) no campeonato'


nome = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))
if nome == '':
    print(ficha(gols = g))
else:
    print(ficha(nome, g))