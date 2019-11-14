#01 -

from random import randint
lista = []
for x in range(10):
    n = randint(1, 100)
    lista.append(n)
    
maior = lista[0]
menor = lista[0]

for x in range(0, 10):
    if maior < lista[x]:
        maior = lista[0]
for x in range(0, 10):
    if menor > lista[x]:
        menor = lista[x]

print(f'''Lista: {lista}
maior número: {maior}
Menor número: {menor}''')

#02 -

from random import randint
lista = []
par = []
impar = []
for x in range(20):
    n = randint(0, 100)
    lista.append(n)
    if lista [x] % 2 == 1:
        impar.append(n)
    else:
        par.append(n)
print(f'LISTA:{lista}')
print(f'PARES:{par}')
print(f'IMPARES:{impar}')

#03 -

from random import randint
vet01 = []
vet02 = []
vet03 = []
for i in range(10):
    n01 = randint(1, 100)
    vet01.append(n01)
    n02 = randint(1, 100)
    vet02.append(n02)
    vet03.append(vet01[i])
    vet03.append(vet02[i])
print(f'''vetor 01: {vet01}
vetor 02: {vet02}
vetor 03: {vet03}''')

#04 -

lista = []
txt = ('''The Python Software Foundation and the global Python community
         welcome and encourage participation by everyone.
         Our community is based on mutual respect, tolerance,
         and encouragement, and we are working to help each
         other live up to these principles.
         We want our community to be more diverse:
         whoever you are, and whatever your background, we welcome you.''')
txt = txt.lower()
txt = txt.replace('.', ' ').replace(',',' ').replace(':', ' ')
lista = txt.split()
for i in lista:
    if i[0] in 'python' or i[-1] in 'python':
        print(i)

#05 -

frase = ('''The Python Software Foundation and the global Python community
            welcome and encourage participation by everyone.
            Our community is based on mutual respect, tolerance,
            and encouragement, and we are working to help each
            other live up to these principles.
            We want our community to be more diverse:
            whoever you are, and whatever your background, we welcome you.''').lower()

frase = frase.replace('.', ' ').replace(',', ' ').replace("'", ' ')
fr = frase.split()
lista = []
for i in fr:
    if len(i) > 4 and (i[0] in 'python' or i[-1] in 'python'):
        lista.append(i)
print(lista)
print(len(lista))
