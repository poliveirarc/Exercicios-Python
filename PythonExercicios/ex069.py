maiores = homens = mulhermais20 = 0
while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F]')).upper().strip()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).upper().strip()[0]
    if idade >= 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulhermais20 += 1
    resp = str(input('Você quer continuar? [S/N]')).upper().strip()[0]
    while resp not in 'SN':
        resp = str(input('Você quer continuar? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maiores}')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'E temos {mulhermais20} mulheres com menos de 20 anos')
