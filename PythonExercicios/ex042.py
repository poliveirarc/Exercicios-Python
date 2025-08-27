seg1 = float(input('Primeiro segmento: '))
seg2 = float(input('Segundo segmento: '))
seg3 = float(input('Terceiro segmento: '))
if seg1 + seg2 > seg3 and seg2 + seg3 > seg1 and seg3 + seg1 > seg2:
    if seg1 == seg2 and seg2 == seg3:
        tipo = 'EQUILÁTERO'
    elif seg1 == seg2 or seg1 == seg3:
        tipo = 'ISÓSCELES'
    else:
        tipo = 'ESCALENO'
    print('Os três segmentos PODEM formar um triângulo e ele será {}.'.format(tipo))
else:
    print('Os segmentos NÃO PODEM formar um triângulo.')