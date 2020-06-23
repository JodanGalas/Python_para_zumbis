# 01 - Identificação de um triangulo.

a = int(input('Insira o primeiro lado de um triangulo: '))
b = int(input('Insira o segundo lado de um triangulo: '))
c = int(input('Insira o terceiro lado de um triangulo: '))

if a > (b + c) or b > (a + c) or c > (a + b):
    print ('Não pode ser um triangulo')
elif a == b == c:
	print ('Todos os lados iguais. triangulo equilátero.')
elif a == b or a == c or b == c:
	print ('Dois lados iguais. triangulo isósceles')
else:
	print ('Todos os lados diferentes. Triangulo escaleno')