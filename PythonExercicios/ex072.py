contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n = int(input('Digite um número de 0 a 20: '))
while n < 0 or n > 20:
    n= int(input('Número inválido! Digite um número de 0 a 20: '))
print(f'Você digitou o número {contagem[n]}.')
