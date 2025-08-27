aluno = {'nome':str(input('Nome do aluno: ')), 'media':float(input('Média do aluno: '))}
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

for l,m in aluno.items():
    print (f'{l} é igual a {m}')


