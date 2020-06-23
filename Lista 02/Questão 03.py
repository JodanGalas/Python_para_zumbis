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