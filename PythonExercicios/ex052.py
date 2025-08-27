num = int(input('Digite um número: '))
total = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[31m{}\033[m'.format(c), end = ' ')
        total += 1
    else:
        print('\033[34m{}\033[m'.format(c), end = ' ')
print('\nO número {} foi divisível {} vezes.'.format(num, total))
if total == 2:
    print('Por isso ele é PRIMO.')
else:
    print('Por isso ele NÃO É PRIMO.')
