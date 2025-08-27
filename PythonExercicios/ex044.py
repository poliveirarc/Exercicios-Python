valorcompra = float(input('Valor da compra: R$'))
print ('')
print('''Formas de pagamento
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão de crédito
[ 3 ] 2x no cartão de crédito
[ 4 ] 3x ou mais no cartão de crédito''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    desconto = valorcompra * 10/100
    print('A compra de R${:.2f} saíra R${:.2f} à vista no dinheiro/cheque. (10% de desconto)'.format(valorcompra, valorcompra - desconto))
elif opcao == 2:
    desconto = valorcompra * 5/100
    print('A compra de R${:.2f} saíra R${:.2f} à vista no cartão de crédito. (5% de desconto)'.format(valorcompra, valorcompra - desconto))
elif opcao == 3:
    print('A compra de R${:.2f} será feita em 2 parcelas de R${:.2f}.'.format(valorcompra, valorcompra / 2))
elif opcao == 4:
    parcelas = int(input('Qual a quantidade de parcelas?: '))
    acrescimo = valorcompra * 20/100
    print('A compra de R${:.2f} será feita em {} parcelas de R${:.2f} (20% de acréscimo).'.format(valorcompra, parcelas, (valorcompra + acrescimo) / parcelas))
else:
    print('OPÇÃO INVÁLIDA!')
