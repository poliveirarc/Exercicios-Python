def leiaInt(n):
    valor = 0
    ok = False
    while True:
        teste = input(n)
        if teste.isnumeric():
            valor = teste
            ok = True
        else:
            print('ERRO! Digite um valor inteiro válido!')
        if ok:
            break
    return valor

numero = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {numero}')