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