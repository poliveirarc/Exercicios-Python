n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite um último número: '))
n = (n1, n2, n3, n4)
print(f'O valor 9 apareceu {n.count(9)} vezes.')
if 3 in n:
    print(f'O valor 3 apareceu na {n.index(3)+1}ª posição.')
print('Os valores pares digitados foram: ', end='')
for c in n:
    if c % 2 == 0:
        print(c, end=' ')