def cabeçalho(msg):
    print('\033[42m^' * len(msg))
    print(f'\033[42m{msg}')
    print('\033[42m^' * len(msg))
    print('\033[0m')


def exibeCabeçalho(msg):
    print('\033[44m^' * len(msg))
    print(f'{msg}')
    print('\033[44m^' * len(msg))
    print('\033[0m')


def exibeFunção(função):
    print(f'\033[45m')
    help(função)
    print('\033[0m')


def exibeFim(msg):
    print('\033[41m^' * len(msg))
    print(f'\033[41m{msg}')
    print('\033[41m^' * len(msg))
    print('\033[0m')


while True:
    cabeçalho('Sistema de ajuda PyHelp')
    func = str(input('Função ou Biblioteca >')).lower().strip()
    if func == 'fim':
        break
    exibeCabeçalho(f'Acessando o manual do comando "{func}"')
    exibeFunção(func)

exibeFim('ATÉ LOGO!')
