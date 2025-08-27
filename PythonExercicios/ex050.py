soma = 0
for c in range(1,7):
    num = int(input('Digite o {}o valor: '.format(c)))
    if num % 2 == 0:
        soma += num
print('A soma dos valores pares digitados é: {}'.format(soma))