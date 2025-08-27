from datetime import datetime
maiores = 0
menores = 0
for c in range(1,8):
    nasc = int(input('Digite o ano de nascimento da {}a pessoa: '.format(c)))
    idade = datetime.now().year - nasc
    if idade >= 21:
        maiores +=1
    else:
        menores +=1
print('Foram digitadas {} pessoas maiores de idade'.format(maiores))
print('Foram digitadas {} pessoas menores de idade'.format(menores))
