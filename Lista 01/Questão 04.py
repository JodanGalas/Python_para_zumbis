#04 - aumento de sálario

salario = int(input('Indique o seu salário: '))
aumento = int(input('Indique a porcentagem de aumento: '))
calculo = salario * aumento/100
novo_salario = salario + aumento
print(f' Seu aumento é de {calculo} e o valor atual do seu salário é de: {novo_salario}')