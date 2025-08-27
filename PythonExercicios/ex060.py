fatorial = 1
num = int(input('Digite um número para calcular seu fatorial: '))
print('Calculando {}! = '. format(num), end ='')
while num != 0:
    print(num, end =' ')
    if num != 1:
        print('x ', end = '')
    else:
        print('= ', end = '')
    fatorial *= num
    num -= 1
print(fatorial)