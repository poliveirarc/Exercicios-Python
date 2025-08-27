resp = 'S'
maior = menor = cont = soma = 0
while resp == 'S':
    num = int(input('Digite um número: '))
    if cont == 0:
        maior = menor = num
    else:
        if num >= maior:
            maior = num
        if num <= menor:
            menor = num
    cont += 1
    soma += num
    resp = str(input('Você quer continuar? [S/N]: ')).upper()
media = soma / cont
print('Você digitou {} números e a média foi {:.2f}.'.format(cont, media))
print('O maior valor digitado foi {} e o menor foi {}.'.format(maior, menor))



