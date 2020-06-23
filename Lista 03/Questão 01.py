#01 -

nota = int(input('Insira uma nota de 0 a 10: '))

while nota < 7:
    print('Nota inválida')
    nota = int(input('Insira uma nota: '))
if nota >= 7:
    print('Nota válida')