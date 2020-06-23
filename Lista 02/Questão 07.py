#07 - latas de tintas

area = int(input('Informa o espaço em metros: '))
if area % 54 != 0:
    lata = int(area / 54) + 1 
else:
    lata = (area / 54)
valor = lata * 80
print(f'Compre {lata} latas. Isso vai lhe custar {valor} reais.')