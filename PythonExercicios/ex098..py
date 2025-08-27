from time import sleep


def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if inicio > fim and passo < 0:
        passo *= (-1)
    if inicio > fim:
        cont = inicio
        while cont >= fim:
            print(cont, end=' ')
            cont -= passo
    else:
        cont = inicio
        while cont <= fim:
            print(cont, end=' ')
            cont += passo
    print('FIM')

print('-='*20)
print('Contagem de 1 até 10 de 1 em 1')
contador(1, 10, 1)
print('-='*20)
print('Contagem de 10 até 0 de 2 em 2')
contador(10, 0, 2)
print('-='*20)
print('Agora é a sua vez de personalizar a contagem:')
i = int(input('Início:' ))
f = int(input('Fim: '))
p = int(input('Passo: '))
if p == 0:
    p = 1
if i > f and p > 0:
    p *= (-1)
contador(i, f, p)