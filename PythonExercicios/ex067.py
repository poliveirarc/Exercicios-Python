while True:
    valor = int(input('Quer ver a tabuada de qual valor?: '))
    if valor < 0:
        break
    print('-' * 40)
    for c in range(1,11):
        print(f'{valor} x {c} = {valor * c}')
    print('-' * 40)
print('-' * 40)
print('PROGRAMA ENCERRADO! Volte sempre!')
