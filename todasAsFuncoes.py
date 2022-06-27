from time import sleep
from TabelaHash import mostrarProdutos, pesquisarNome
from TabelaHash import *

def login():
    usuario = 'romulo'
    senha = '123456'
    novo_user = input('Usuário: ').lower().strip()
    nova_password = input('Senha: ')
    if usuario == novo_user and senha == nova_password:
        print('Entrando no sistema')
        trabalhador()
    else:
        resp = ''
        print('LOGIN INVALIDO')
        while resp != 'S':
            resp = input('Deseja cadastrar um novo usuário? [S/N]: ').upper()[0]
            if resp == 'S':
                usuario2 = input('Novo Usuário: ')
                senha2 = input('Nova Senha: ')
                print('Novo login cadastrado!')
                novo_user = input('Usuário: ')
                nova_password = input('Senha: ')
                if usuario == novo_user and senha == nova_password or usuario2 == novo_user and senha2 == nova_password:
                    print('Entrando no sistema')
                    trabalhador()
            else:
                exit()
                

def consumidor():
    print('''
        [ 1 ] Ver todos os produtos [ 1 ]
        [ 2 ]  Pesquisar pelo nome  [ 2 ] 
        [ 3 ]          SAIR         [ 3 ]
''')
    sleep(0.5)
    opcao = input('\033[1;33mResposta: \033[m')
    if opcao == '1':
        sleep(1)
        mostrarProdutos()
    elif opcao == '2':
        sleep(1)
        print(pesquisarNome(produto2))
    elif opcao == '3':
        sleep(0.5)
        exit()
    else:
        while opcao not in '123':
            sleep(0.3)    
            print('\033[1;31m OPÇÃO INVÁLIDA \033[m')
            sleep(0.2)
            opcao = input('\033[1;33mQual sua Resposta? \033[m')
            if opcao == '1':
                sleep(1)
                mostrarProdutos()
                consumidor()
            elif opcao == '2':
                sleep(1)
                print(pesquisarNome(produto2))
                consumidor()
            elif opcao == '3':
                sleep(0.5)
                exit()
    consumidor()
   
def trabalhador():
    print('''
        [ 1 ] Adicionar um produto  [ 1 ]
        [ 2 ]  Remover um produto   [ 2 ] 
        [ 3 ] Ver todos os produtos [ 3 ]
        [ 4 ]  Pesquisar pelo nome  [ 4 ]
        [ 5 ]        SAIR           [ 5 ]
''')
    opcao = input('\033[1;33mResposta: \033[m')
    if opcao == '1':
        sleep(1)
        adicionarProduto(produto2)
    elif opcao == '2':
        sleep(1)
        print(' remover um produto da tabela hash')
    elif opcao == '3':
        sleep(1)
        mostrarProdutos()
    elif opcao == '4':
        sleep(1)
        print(pesquisarNome(produto2))
    elif opcao == '5':
        sleep(0.5)
        exit()
    else:
        while opcao not in '12345':        
            print('\033[1;31m OPÇÃO INVÁLIDA \033[m')
            opcao = input('\033[1;33mQual sua Resposta? \033[m')
            if opcao == '1':
                sleep(1)
                adicionarProduto(produto2)
            elif opcao == '2':
                sleep(1)
                print(' remover um produto da tabela hash')
            elif opcao == '3':
                sleep(1)
                mostrarProdutos()
            elif opcao == '4':
                sleep(1)
                print(pesquisarNome(produto2))
            elif opcao == '5':
                sleep(0.5)
                exit()
    trabalhador()

produto2 = {}