soma = cont = valor = 0
valor = float(input('Digite um valor [999 para sair]: '))
while valor != 999:
    soma += valor
    cont += 1
    valor = float(input('Digite um valor [999 para sair]: '))
print('Você digitou {} números e a soma deles foi {}.'.format(cont, soma))
