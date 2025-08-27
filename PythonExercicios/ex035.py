print('-=-'*20)
print('ANALISADOR DE TRIÂNGULOS')
print('-=-'*20)
lado1 = float(input('Digite a medida do primeiro lado: '))
lado2 = float(input('Digite a medida do segundo lado: '))
lado3 = float(input('Digite a medida do terceiro lado: '))
if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado3 + lado1 > lado2:
    print('Os segmentos acima PODEM formar um triângulo')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo')