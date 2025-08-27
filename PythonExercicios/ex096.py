def área(a,b):
    area = a * b
    print(f'A área de um terreno de {a}m x {b}m é igual a {area}m².')


print('CÁLCULO DE ÁREA DE UM TERRENO')
print('-'*30)

x = float(input('Qual a largura do terreno? (metros)'))
y = float(input('Qual o comprimento do terreno? (metros)'))
área(x,y)