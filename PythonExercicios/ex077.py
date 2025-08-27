palavras = ('casa', 'verdade', 'amor', 'familia', 'cachorro', 'felicidade')
for c in palavras:
    print(f'\nNa palavra {c.upper()} temos as vogais ', end=' ')
    for vogal in c:
        if vogal in 'aeiou':
            print(vogal, end='')
