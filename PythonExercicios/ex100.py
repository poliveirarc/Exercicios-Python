from random import randint


def sorteia():
    for i in range(0,5):
        n = randint(0,10)
        números.append(n)


def somaPar(num):
    soma = 0
    for n in num:
        if n % 2 == 0:
            soma += n
    print(f'A soma dos valores pares é {soma}')


números = list()
sorteia()
print(f'Os números sorteados foram {números}')
somaPar(números)