from time import sleep


def maior (*num):
    cont = mai = 0
    for n in num:
        if cont == 0:
            mai = n
        else:
            if n > mai:
                mai = n
        cont += 1
    print('Analisando os valores...')
    sleep(1)
    print(num)
    sleep(1)
    print(f'Foram digitados {cont} números. E o maior valor é {mai}')


maior (2, 9, 4, 5, 7, 1)
maior (4, 7, 0)
maior (1, 2)
maior (6)
maior ()