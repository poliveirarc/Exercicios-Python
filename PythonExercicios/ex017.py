from math import hypot
catop = float(input('Digite a medida do cateto oposto: '))
catadj = float(input('Digite a medida do cateto adjacente: '))
hipo = hypot(catop, catadj)
print('A hipotenusa vai medir {:.2f}.'.format(hipo))