listageral = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/2
    listageral.append([nome, [nota1, nota2], [media]])
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Você quer continuar? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break
print('-='*20)
print(f'{'Nº':<5} {'NOME':<15} {'MÉDIA':^5}')
print('-'*40)
for c, i in enumerate(listageral):
    print(f'{c:<5}', end ='')
    print(f'{i[0]:<15}', end='')
    print(f'{i[2]}')
while True:
    ind = int(input('Mostrar notas de qual aluno? (999 interrompe)'))
    if ind == 999:
        break
    else:
        if ind <= len(listageral) -1:
            print(f'Notas de {listageral[ind][0]}: {listageral[ind][1]}')