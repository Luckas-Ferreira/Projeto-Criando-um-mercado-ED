from TabelaHash import mostrarProdutos, pesquisarNome
from TabelaHash import *


def login():
    usuario = 'romulo'
    senha = '123456'
    novo_user = input('Usuário: ').lower()
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
    opcao = input('Resposta: ')
    if opcao == '1':
        mostrarProdutos()
    elif opcao == '2':
        print(pesquisarNome())
    elif opcao == '3':
        exit()
    else:
        while opcao not in '123':        
            print('\033[1;31m OPÇÃO INVÁLIDA \033[m')
            opcao = input(' Qual sua resposta? ')
            if opcao == '1':
                mostrarProdutos()
                consumidor()
            elif opcao == '2':
                print(pesquisarNome())
                consumidor()
            elif opcao == '3':
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
    opcao = input('Resposta: ')
    if opcao == '1':
        adicionarProduto()
    elif opcao == '2':
        print(' remover um produto da tabela hash')
    elif opcao == '3':
        mostrarProdutos()
    elif opcao == '4':
        print(pesquisarNome())
    elif opcao == '5':
        exit()
    else:
        while opcao not in '12345':        
            print('\033[1;31m OPÇÃO INVÁLIDA \033[m')
            opcao = input(' Qual sua resposta? ')
            if opcao == '1':
                adicionarProduto()
            elif opcao == '2':
                print(' remover um produto da tabela hash')
            elif opcao == '3':
                mostrarProdutos()
            elif opcao == '4':
                print(pesquisarNome())
            elif opcao == '5':
                exit()
    trabalhador()