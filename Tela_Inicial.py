from todasAsFuncoes import *

def telaInicial():
    print('MERCADINHO DO RÔMULO')
    print ('''
    Você é consumidor ou trabalhar no mercado? \n
            [ 1 ]  Consumidor  [ 1 ]
            [ 2 ] Trabalhador  [ 2 ] 
            [ 3 ]     SAIR     [ 3 ] \n''')
    opção = input(' Resposta: ')
    if opção == '1':
        consumidor()
    elif opção == '2':
        login()
    elif opção == '3':
        exit()
    else:
        while opção not in '123':        
            print('\033[1;31m OPÇÃO INVÁLIDA \033[m')
            opção = input(' Qual sua resposta? ')
            if opção == '1':
                consumidor()
            elif opção == '2':
                trabalhador()
            elif opção == '3':
                exit()

#Inicil do programa
telaInicial()