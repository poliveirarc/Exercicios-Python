def fatorial(n, show = False):
    '''
    Função que calcula o fatorial de um número.
    :param n: número a ser calculado o fatorial
    :param show: True = exibe cálculo / False = oculta cálculo. Padrão = False
    :return: fatorial do número n
    '''
    fat = 1
    for c in range(n, 0, -1):
        if show == True:
            if c == 1:
                print(f'{c} = ', end = ' ')
            else:
                print(f'{c} x ', end= '')
        fat = fat * c
    return fat


print(fatorial(3, show = True))
