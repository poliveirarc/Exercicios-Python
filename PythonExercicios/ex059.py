from time import sleep
opcao = 0
maior = 0
valor1 = float(input('Primeiro valor: '))
valor2 = float(input('Segundo valor: '))
while opcao != 5:
    print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
    opcao = int(input('>>> Qual é sua opção?: '))
    if opcao == 1:
        soma = valor1 + valor2
        print('A soma entre {} e {} é igual a {}.'.format(valor1, valor2, soma))
    elif opcao == 2:
        mult = valor1 * valor2
        print('A multiplicação entre {} e {} é igual a {}.'.format(valor1, valor2, mult))
    elif opcao == 3:
        if valor1 > valor2:
            maior = valor1
        else:
            maior = valor2
        print('Entre {} e {} o maior valor é {}.'.format(valor1, valor2, maior))
    elif opcao == 4:
        print('Informe os números novamente: ')
        valor1 = float(input('Primeiro valor: '))
        valor2 = float(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida! Tente novamente!')
sleep(2)
print('Fim do programa. Volte sempre!')
