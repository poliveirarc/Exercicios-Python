sexo = str(input('Informe seu sexo: ')).strip().upper()
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe se sexo [M/F]: ')).strip().upper()
print('Sexo {} registrado com sucesso!'.format(sexo))

