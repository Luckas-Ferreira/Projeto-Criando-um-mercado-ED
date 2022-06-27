from todasAsFuncoes import *
from time import sleep


def telaInicial():
    sleep(0.8)
    print('\t\t\tMERCADINHO DO RÔMULO')
    sleep(0.5)
    print ('''
    Você é consumidor ou trabalhar no mercado? \n
    
            [ 1 ]  Consumidor  [ 1 ]
            [ 2 ] Trabalhador  [ 2 ] 
            [ 3 ]     SAIR     [ 3 ] \n''')
    opção = input('\033[1;33mResposta: \033[m')
    if opção == '1':
        sleep(1)
        consumidor()
    elif opção == '2':
        sleep(1)
        login()
    elif opção == '3':
        sleep(0.5)
        exit()
    else:
        while opção not in '123':        
            print('\033[1;31m OPÇÃO INVÁLIDA \033[m')
            opção = input('\033[1;33mQual sua Resposta? \033[m')
            if opção == '1':
                sleep(1)
                consumidor()
            elif opção == '2':
                sleep(1)
                login()
            elif opção == '3':
                sleep(0.5)
                exit()

#Inicil do programa
telaInicial()