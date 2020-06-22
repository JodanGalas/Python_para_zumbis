#05 - desconto

produto = float(input('Indique o preço do seu produto: '))
desconto = int(input('Indique a quantidade de desconto: '))
calculo = produto* desconto/100
preco = produto - desconto
print(f' Seu desconto é de {calculo} e o valor atual do seu produto é de: {preco}')