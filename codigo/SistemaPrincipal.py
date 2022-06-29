from time import sleep
from TabelaHash import mostrarProdutos, pesquisarNome
from TabelaHash import *
import sys



def Titulo():
    titulo = cor.green() + "\n\t       MERCADINHO DO RÔMULO \n" + cor.close()
    for i in list(titulo):
        print(i, end='')
        sys.stdout.flush()
        sleep(0.1)

def login():
    usuario = 'romulo'
    senha = '123456'
    novo_user = input(cor.green() + 'Usuário: ' + cor.close()).lower().strip()
    nova_password = input(cor.green() + 'Senha: ' + cor.close())
    if usuario == novo_user and senha == nova_password:
        print(cor.yellow() + '\n\t       ENTRANDO NO SISTEMA' + cor.close())
        sleep(1)
        trabalhador()
    else:
        resp = ''
        print(cor.red() + '\nLOGIN INVALIDO' + cor.close())
        while resp != 'S':
            sleep(0.5)
            resp = input(cor.yellow() + 'Deseja cadastrar um novo usuário? [S/N]: ' + cor.close()).upper()[0]
            if resp == 'S':
                usuario2 = input(cor.green() + '\nNovo Usuário: ' + cor.close())
                senha2 = input(cor.green() + 'Nova Senha: ' + cor.close())
                print(cor.red() + 'Novo login cadastrado!' + cor.close())
                novo_user = input(cor.green() + 'Usuário: ' + cor.close())
                nova_password = input(cor.green() + 'Senha: ' + cor.close())
                if usuario == novo_user and senha == nova_password or usuario2 == novo_user and senha2 == nova_password:
                    print(cor.yellow() + 'Entrando no sistema' + cor.close())
                    trabalhador()
            else:
                telaInicial()
                

def consumidor():
    print(cor.red() + '\n\t\t TELA DO CLIENTE' + cor.close())
    sleep(0.5)
    print('''
        [ 1 ] Ver todos os produtos [ 1 ]
        [ 2 ]  Pesquisar pelo nome  [ 2 ] 
        [ 3 ] Voltar../ Tela Inicial[ 3 ]
        [ 4 ]         SAIR          [ 4 ]
''')
    sleep(0.5)
    opcao = input('\033[1;33mResposta: \033[m').lower().strip()
    if opcao == '1' or opcao == 'ver':
        sleep(1)
        mostrarProdutos()
    elif opcao == '2' or opcao == 'pesquisar':
        sleep(1)
        print(pesquisarNome(produto2))
    elif opcao == '3' or opcao == 'voltar':
        telaInicial()
    elif opcao == '4' or opcao == 'sair':
        sleep(0.5)
        exit()
    else:
        while opcao not in '123':
            sleep(0.3)    
            print('\033[1;31m OPÇÃO INVÁLIDA \033[m')
            sleep(0.2)
            opcao = input('\033[1;33mQual sua Resposta? \033[m')
            if opcao == '1' or opcao == 'ver':
                sleep(1)
                mostrarProdutos()
            elif opcao == '2' or opcao == 'pesquisar':
                sleep(1)
                print(pesquisarNome(produto2))
            elif opcao == '3' or opcao == 'voltar':
                telaInicial()
            elif opcao == '4' or opcao == 'sair':
                sleep(0.5)
                exit()
    consumidor()
   
def trabalhador():
    print(cor.red() + '\n\t       TELA DO FUNCIONARIO' + cor.close())
    sleep(0.5)
    print('''
        [ 1 ] Adicionar um produto  [ 1 ]
        [ 2 ]  Remover um produto   [ 2 ] 
        [ 3 ] Ver todos os produtos [ 3 ]
        [ 4 ]  Pesquisar pelo nome  [ 4 ]
        [ 5 ] Voltar../ Tela Inicial[ 5 ]
        [ 6 ]        SAIR           [ 6 ]
''')
    opcao = input('\033[1;33mResposta: \033[m')
    if opcao == '1' or opcao == 'adicionar':
        sleep(1)
        adicionarProduto(produto2)
    elif opcao == '2' or opcao == 'remover':
        sleep(1)
        print(' remover um produto da tabela hash')
    elif opcao == '3' or opcao == 'ver':
        sleep(1)
        mostrarProdutos()
    elif opcao == '4' or opcao == 'pesquisar':
        sleep(1)
        print(pesquisarNome(produto2))
    elif opcao == '5' or opcao == 'voltar':
        telaInicial()
    elif opcao == '6' or opcao == 'sair':
        sleep(0.5)
        exit()
    else:
        while opcao not in '12345':        
            print('\033[1;31m OPÇÃO INVÁLIDA \033[m')
            opcao = input('\033[1;33mQual sua Resposta? \033[m')
            if opcao == '1' or opcao == 'adicionar':
                sleep(1)
                adicionarProduto(produto2)
            elif opcao == '2' or opcao == 'remover':
                sleep(1)
                print(' remover um produto da tabela hash')
            elif opcao == '3' or opcao == 'ver':
                sleep(1)
                mostrarProdutos()
            elif opcao == '4' or opcao == 'pesquisar':
                sleep(1)
                print(pesquisarNome(produto2))
            elif opcao == '5' or opcao == 'voltar':
                telaInicial()
            elif opcao == '6' or opcao == 'sair':
                sleep(0.5)
                exit()
    trabalhador()

produto2 = {}

def telaInicial():
    Titulo()
    sleep(0.5)
    print(cor.red() + '\n    Você é consumidor ou trabalhar no mercado?' + cor.close())
    sleep(0.5)
    print ('''
             [ 1 ]  Consumidor  [ 1 ]
             [ 2 ] Trabalhador  [ 2 ] 
             [ 3 ]     SAIR     [ 3 ] \n''')
    
    sleep(0.5)
    opção = input('\033[1;33mResposta: \033[m').lower().strip()
    if opção == '1' or opção == 'consumidor':
        sleep(1)
        consumidor()
    elif opção == '2' or opção == 'trabalhador':
        sleep(1)
        login()
    elif opção == '3' or opção == 'sair':
        sleep(0.5)
        exit()
    else:
        while opção not in '123':        
            print('\033[1;31m OPÇÃO INVÁLIDA \033[m')
            opção = input('\033[1;33mQual sua Resposta? \033[m')
            if opção == '1' or opção == 'consumidor':
                sleep(1)
                consumidor()
            elif opção == '2' or opção == 'trabalhador':
                sleep(1)
                login()
            elif opção == '3' or opção == 'sair':
                sleep(0.5)
                exit()

#Inicil do programa
telaInicial()