valorcasa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
nparcelas = int(input('Quanto anos de financiamento?: '))
vparcela = valorcasa/(nparcelas*12)
print('Para pagar uma casa de R${:.2f} em {} anos, o valor da parcela será de R${:.2f}.'.format(valorcasa, nparcelas, vparcela))
if vparcela <= salario*30/100:
    print('Empréstimo \033[32mCONCEDIDO\033[m!')
else:
    print('Empréstimo \033[31mNEGADO\033[m!')
