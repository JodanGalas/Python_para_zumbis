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