print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
c = 1
soma = 10
termo = primeiro
while c <= 10:
    print(termo, '-> ', end='')
    termo += razao
    c += 1
print('PAUSA')
resposta = int(input('Quantos termos a mais vc quer mostrar?: '))
soma += resposta
while resposta != 0:
    c = 1
    while c <= resposta:
        print(termo, '-> ', end='')
        termo += razao
        c += 1
    print('PAUSA')
    resposta = int(input('Quantos termos a mais vc quer mostrar?: '))
    soma += resposta
print('Progressão finalizada com {} termos mostrados.'.format(soma))