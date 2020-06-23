#06 - salário

ganho = float(input('Quanto você ganha por hora? '))
horas = int(input('Quantas horas você trabalha por mês: '))

salariob = ganho * horas
ir = salariob * 0.11
inss = salariob * 0.08
sindicato = salariob * 0.05
salariol = salariob - ir - inss - sindicato

print (f'+ Salário Bruto : R$ {salariob}')
print (f'- IR: R$ {ir}')
print (f'- INSS: R$ {inss}')
print (f'- Sindicato: R$ {sindicato}')
print (f'= Salário Liquido : R$ {salariol}')