nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print('A média do aluno é de {}. \nAluno REPROVADO'.format(media))
elif (media >= 5) and (media < 7):
    print('A média do aluno é de {}. \nAluno EM RECUPERAÇÂO'.format(media))
else:
    print('A média do aluno é de {}. \nAluno APROVADO'.format(media))
