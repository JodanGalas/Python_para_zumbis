#05 -
n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
if n1 < n2:
    
    n1 = n2
    n2 = n1

resto = n1 % n2
mdc = n2

while resto != 0:
	resto = mdc % resto
	mdc = resto
	
print (f'O mdc de {n1,n2} é: {mdc}')