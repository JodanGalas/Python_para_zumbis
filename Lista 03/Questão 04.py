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