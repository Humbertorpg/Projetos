#aula 40
#operadores logicos
 
entrada = input('[E]entrar [S]sair')
senha_digitada = input('senha: ')

senha_permitida = '123456'
if entrada == 'E' or entrada == 'e' and senha_digitada == senha_permitida:
    print('entrar')
else:
    print('sair')
