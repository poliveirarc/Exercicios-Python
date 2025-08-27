def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return f'Com {idade} anos: AINDA NÃO PODE VOTAR'
    elif 16 <= idade < 18 or idade > 80:
        return f'Com {idade} anos: VOTO FACULTATIVO'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


print('-'*30)
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))