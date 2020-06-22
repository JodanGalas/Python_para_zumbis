#03 - conversão em minutos

dia = int(input('Informe a quantidade de dias: '))
hora = int(input('Informe a quantidade de horas: '))
minuto = int(input('Informe a quantidade de minutos: '))
segundo = int(input('Informe a quantidade de segundos: '))
calculo = dia*24 + hora*3600 + minuto*60 + segundo
print(f'Seu tempo convertido em segundos é de: {calculo}')