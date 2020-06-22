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

# 02 - Ano bissexto
    
ano = int(input('Informe um ano: '))
if ano%4 == 0 and (ano%100 != 0 or ano%400 == 0):
    print('Esse ano é Bissexto')
    
else:
    print('Esse ano não é bissexto')

#03 - Rendimento díario.

peso = int(input('Informe o peso do peixe: '))
excesso = peso - 50
multa = excesso * 4
if peso <= 50:
    print(f'''Você não excedeu o peso padrão e não vai levar multa.
Excesso: {0}Kg
Multa: {0} R$''')
    
if peso > 50 :
    print(f'Você excedeu {excesso}kg e sua multa será de {multa}R$.')

#04 - Maior número.

n1 = int(input('Insira um número: '))
n2 = int(input('Insira outro número: '))
n3 = int(input('Insira outro número: '))

if n1 > n2 and n1 > n3 :
    print(f'{n1} é o maior número.')

elif n2 > n1 and n2 > n3 :
    print(f'{n2} é o maior número.')

elif n3 > n1 and n3 > n2:
    print(f'{n3} é o maior número.')

else:
    print('Todos os números são iguais.')

# 05 - Maior e menor número.

n1 = int(input('Insira um número: '))
n2 = int(input('Insira outro número: '))
n3 = int(input('Insira outro número: '))

if n1 < n2 and n1 < n3 :
    print(f'{n1} é o menor número.')

elif n2 < n1 and n2 < n3 :
    print(f'{n2} é o menor número.')

elif n3 < n1 and n3 < n2:
    print(f'{n3} é o menor número.')


if n1 > n2 and n1 > n3 :
    print(f'{n1} é o maior número.')

elif n2 > n1 and n2 > n3 :
    print(f'{n2} é o maior número.')

elif n3 > n1 and n3 > n2:
    print(f'{n3} é o maior número.')

else:
    print('Todos os números são iguais.')
    
#06 - salário

ganho = float(input('Quanto você ganha por hora? '))
horas = int(input('Quantas horas você trabalha por mês: '))

salariob = ganho * horas
ir = salariob * 0.11
inss = salariob * 0.08
sindicato = salariob * 0.05
salariol = salariob - ir - inss - sindicato

print (f'+ Salário Bruto : R$ {salariob}')
print (f'- IR: R$ {ir}')
print (f'- INSS: R$ {inss}')
print (f'- Sindicato: R$ {sindicato}')
print (f'= Salário Liquido : R$ {salariol}')

#07 - latas de tintas

area = int(input('Informa o espaço em metros: '))
if area % 54 != 0:
    lata = int(area / 54) + 1 
else:
    lata = (area / 54)
valor = lata * 80
print(f'Compre {lata} latas. Isso vai lhe custar {valor} reais.')
    
    




    
 

        
                



        
        
