frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira posição na qual o A aparece é: {}'.format(frase.find('A')+1))
print('A última posição na qual o A aparece é: {}'.format(frase.rfind('A')+1))