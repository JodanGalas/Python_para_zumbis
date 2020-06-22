#09 - diaria

distancia = int(input('Indique a quantidade de km percorridos pelo seu carro alugado: '))
dias_alugados = int(input('Indique a quantidade de dias que você alugou o carro: '))
diaria = (dias_alugados*60) + distancia * 0.15
print(f'No final de tudo você pagará {diaria}$')