def notas(*nota, sit = False):
    avaliação = dict()
    avaliação['total'] = len(nota)
    avaliação['maior'] = max(nota)
    avaliação['menor'] = min(nota)
    avaliação['média'] = sum(nota) / len(nota)
    if sit == True:
        if avaliação['média'] > 7:
            avaliação['situação'] = 'BOA'
        else:
            avaliação['situação'] = 'RUIM'
    return avaliação


resp = notas(10, 5.5, 2.5, 9, 8.5, sit=True)
print(resp)