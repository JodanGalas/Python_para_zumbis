#10 - dias perdidos por fumar cigarro

cigarros = int(input('Quantos cigarros você fuma por dia?'))
anos = int(input('Já faz quantos anos que você fuma?'))
minutos_anos = ((cigarros * 365) + (anos * 365))*(24*60)
perda = minutos_anos/(24*60)
print(f'Atualmente você já perdeu {perda} dias de vida!')