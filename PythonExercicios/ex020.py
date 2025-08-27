from random import shuffle
nome1 = input('Primeiro aluno: ')
nome2 = input('Segundo aluno: ')
nome3 = input('Terceiro aluno: ')
nome4 = input('Quarto aluno: ')
lista = [nome1, nome2, nome3, nome4]
escolhido = shuffle(lista)
print('O orden escolhida foi: ')
print(lista)