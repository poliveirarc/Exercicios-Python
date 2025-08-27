from datetime import date
empregado = dict()
empregado['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
empregado['idade'] = date.today().year - nasc
empregado['CTPS'] = int(input('Carteira de trabalho (0 não tem): '))
if empregado['CTPS'] != 0:
    empregado['contratação'] = int(input('Ano de contratação: '))
    empregado['salário'] = float(input('Salário: R$'))
    empregado['aposentadoria'] = empregado['idade'] + ((empregado['contratação'] + 35) - date.today().year)
for l, m in empregado.items():
    print(f'{l} tem o valor {m}.')
