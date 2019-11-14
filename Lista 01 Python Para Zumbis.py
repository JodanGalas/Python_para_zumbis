#01 - soma de dois números

n1 = int(input('Insira um número'))
n2 = int(input('Insira outro número'))
soma = n1+n2
print(f'A soma dos números é: {soma}')

#02 - conversão de metros para milímetros

metro = int(input('Insira um valor em metros: '))
conversao = metro * 1000
print(f'O valor escolhido é igual a {conversao}mm')

#03 - conversão em minutos

dia = int(input('Informe a quantidade de dias: '))
hora = int(input('Informe a quantidade de horas: '))
minuto = int(input('Informe a quantidade de minutos: '))
segundo = int(input('Informe a quantidade de segundos: '))
calculo = dia*24 + hora*3600 + minuto*60 + segundo
print(f'Seu tempo convertido em segundos é de: {calculo}')

#04 - aumento de sálario

salario = int(input('Indique o seu salário: '))
aumento = int(input('Indique a porcentagem de aumento: '))
calculo = salario * aumento/100
novo_salario = salario + aumento
print(f' Seu aumento é de {calculo} e o valor atual do seu salário é de: {novo_salario}')

#05 - desconto

produto = float(input('Indique o preço do seu produto: '))
desconto = int(input('Indique a quantidade de desconto: '))
calculo = produto* desconto/100
preco = produto - desconto
print(f' Seu desconto é de {calculo} e o valor atual do seu produto é de: {preco}')

#06 - tempo de viagem

distancia = int(input('Insira a distacia à percorrer: '))
velocidade_media = int(input('Insira a velocidade media do seu veículo: '))
tempo_viagem = distancia/velocidade_media
print(f'O tempo da sua viagem será de aproximadamente {tempo_viagem}hrs')

#07 - conversão de celsius para fahrenheit

celsius = int(input('Insira uma temperatura em graus celsius: '))
conversao = (9*celsius)/5 + 32
print(f'convertendo para fahrenheit, sua nova temperatura é de: {conversao}F')

#08 - conversão de fahrenheit para celsius

fahrenheit = int(input('Insira uma temperatura em graus fahrenheit: '))
conversao = (fahrenheit)/(9/5) - 32
print(f'convertendo para celsius, sua nova temperatura é de: {conversao}C')

#09 - diaria

distancia = int(input('Indique a quantidade de km percorridos pelo seu carro alugado: '))
dias_alugados = int(input('Indique a quantidade de dias que você alugou o carro: '))
diaria = (dias_alugados*60) + distancia * 0.15
print(f'No final de tudo você pagará {diaria}$')

#10 - dias perdidos por fumar cigarro

cigarros = int(input('Quantos cigarros você fuma por dia?'))
anos = int(input('Já faz quantos anos que você fuma?'))
minutos_anos = ((cigarros * 365) + (anos * 365))*(24*60)
perda = minutos_anos/(24*60)
print(f'Atualmente você já perdeu {perda} dias de vida!')

#11 - calculo de digitos

potencia = len(str(2**1000000))

print(f' Dois elevado a potência de um milhão tem exatamente {potencia} digitos.')
