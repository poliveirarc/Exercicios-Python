frase = str(input('Digite uma frase: ')).strip().upper()
s_espaço = frase.replace(' ', '')
inverso = s_espaço.upper()[::-1]
print('O inverso de {} é {}'.format(s_espaço.upper(), inverso))
if s_espaço == inverso:
    print('Temos um PAlÍNDROMO')
else:
    print('NÃO temos um PAlÍNDROMO')