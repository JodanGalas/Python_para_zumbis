#01 -

nota = int(input('Insira uma nota de 0 a 10: '))

while nota < 7:
    print('Nota inválida')
    nota = int(input('Insira uma nota: '))
if nota >= 7:
    print('Nota válida')

#02 -

usuario = input('Insira o seu usuário: ')
senha = input('Insira sua senha: ')
while usuario == senha:
    print('ERRO! Tente novamente.')
    usuário = input('Usuário: ')
    senha = input('Senha: ')
else:
    print('Login efetuado com sucesso.')
    
#03 -

pais_1 = 80000
pais_2 = 200000
count = 0

while pais_1 <= pais_2:
    pais_1 = pais_1 + (pais_1 * 3/100)
    pais_2 = pais_2 + (pais_2 * 1.5/100)
    count += 1
print(f'''Será necessário {count} anos para que a
população A iguale ou ultrapasse a
população B.''')

#04 -

num = int(input('Insira um número: '))
ultimo = 1
penultimo =1

if num == 1 or num == 2:
    print('1')
else:
    count = 3
    while count <= num:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1
    print(f'F: {termo}')

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


