print('-'*25)
print('SEQUÊNCIA DE FIBONACCI')
print('-'*25)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
c = 2
if n == 1:
    print(t1, '-> ', end = '')
elif n == 2:
    print(t1, '-> ', t2, '-> ', end = '' )
else:
    print(t1, '-> ', t2, '-> ', end = '')
    while c < n:
        t3 = t1 + t2
        print(t3, '-> ', end = '' )
        t1 = t2
        t2 = t3
        c += 1
print('FIM')

