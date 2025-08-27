soma = 0
maisvelho = ''
maioridade = 0
mmenor20 = 0
for c in range(1,5):
    print('-' * 10)
    print('  {}ª PESSOA  '.format(c))
    print('-' * 10)
    nome = str(input('Nome:'))
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]:')).upper()
    if sexo != 'M' and sexo != 'F':
        print('Sexo incorreto!')
        break
    soma += idade
    if idade > maioridade and sexo == 'M':
        maioridade = idade
        maisvelho = nome
    if idade < 20 and sexo == 'F':
        mmenor20 += 1
media = soma/4
print('A média de idade do grupo é de {} anos.'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridade, maisvelho))
print('Ao todo, são {} mulheres com menos de 20 anos.'.format(mmenor20))

