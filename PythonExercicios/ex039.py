from datetime import datetime
ano = int(input('Ano de nascimento: '))
idade = datetime.now().year - ano
print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, datetime.now().year))
if idade < 18:
    tempo = (18 - idade)
    print('Ainda faltam {} anos para o alistamento.'.format(tempo))
    print('Seu alistamento será em {}'.format(datetime.now().year + tempo))
elif idade > 18:
    tempo = (idade - 18)
    print('Você já deveria ter se alistado há {} anos.'.format(tempo))
    print('Seu alistamento foi em {}'.format(datetime.now().year - tempo))
else:
    print('Você tem que se alistar IMEDIATAMENTE')