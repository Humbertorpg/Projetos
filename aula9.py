#aula 45
#formatação basica de  strings
# s - string
# d - int
# f - float
# .<número de digitos>f
# x ou X - hexadecimal
# (caractere)(><^)(quantidade)
# > - esquerda
# < - direita
# ^ - centro
# = - força o numero a aparecer antes do zero
# sinal - + ou -
#  Ex: 0>-100,.1f
#conversion flags - !r !s !a

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
#print(f'{100.84569687414422:0>+10,.1f}')