nome = 'humberto'
altura = 1.75
peso = 109
imc = peso/(altura * altura)

linha_1 = f'{nome} {imc:,.3f}'

print(nome,'tem',altura,'metros de altura,' )
print('pesa', peso,"quilos e seu IMC é:" )
print(linha_1)
print()