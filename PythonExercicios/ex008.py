dist = int(input('Digite a distância em metros: '))
print('{} km \n {} hm \n {} dam \n {} dm \n {} cm \n {} mm '.format((dist/1000), (dist/100), (dist/10), (dist*10), (dist*100), (dist*1000)))