'''
exercicio
peça ao suarioa para digitar seu nome
peça ao usuario para digitrar sus idade
se nome e idade forem digitados:
    exiba:
    seu nome é {nome}
    seu nome invertido é {nome invertido}
    seu nome contem ou não espaços 
    seu nome tem {n} letras
    a pri meira letra do seu nome é {letra}
    a ultima letra do seu nome é {letra}
se nada for digitado em nome ou idade :
    exiba "desculpe, voçe deixou campos vazios."
'''
nome = input('escreva seu nome:')
idade = input('escreva sua idade: ')

if nome and idade :
    print(f'seu nome é {nome}')
    print(f'seu nome invertido é {nome[::-1]}')
    if '' in nome:
        print(f'seu nome contem espaços')
    else:
        print('seu nome não contem espaços')    
    
    print(f'seu nome tem {len(nome)} letras')
    print(f'a pri meira letra do seu nome é {nome[0]}')
    print(f'a ultima letra do seu nome é {nome[-1]}')

else:
    print("desculpe, voçe deixou campos vazios.")