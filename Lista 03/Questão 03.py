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