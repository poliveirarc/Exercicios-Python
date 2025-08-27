pessoas = list()
temp = dict()
somaidade = media = 0
while True:
    temp['nome'] = str(input('Nome: '))
    while True:
        temp['sexo'] = str(input('Sexo: ')).upper().strip()[0]
        if temp['sexo'] in 'MF':
            break
        print('ERRO! Digite somente M ou F.')
    temp['idade'] = int(input('Idade: '))
    pessoas.append(temp.copy())
    temp.clear()
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('ERRO! Digite somente S ou N.')
    if resp == 'N':
        break

print('-'*30)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
for c in range(0, len(pessoas)):
    somaidade += pessoas[c]['idade']
media = somaidade / len(pessoas)
print(f'B) A média de idade é de {media} anos.')
print('As mulheres cadastradas foram ', end='')
for c in range(0, len(pessoas)):
    if pessoas[c]['sexo'] == 'F':
        print(f'{pessoas[c]['nome']}' )
print('Lista das pessoas que estão acima da média:')
for c in range(0,len(pessoas)):
    if pessoas[c]['idade'] > media:
        print(pessoas[c])
