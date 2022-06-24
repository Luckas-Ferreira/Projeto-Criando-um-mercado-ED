def consumidor():
    print('''
     [ 1 ] Ver todos os produtos [ 1 ]
     [ 2 ]  Pesquisar pelo nome  [ 2 ] 
     [ 3 ]         SAIR          [ 3 ]
''')
    opcao = input('Resposta: ')
    if opcao == '1':
        print('imprime a tabela hash')
    elif opcao == '2':
        print(' Busca na tabela hash')
    elif opcao == '3':
        exit()
    else:
        while opcao not in '123':        
            print('\033[1;31m OPÇÃO INVÁLIDA \033[m')
            opcao = input(' Qual sua resposta? ')
            if opcao == '1':
                print('imprime a tabela hash')
            elif opcao == '2':
                print('busca na tabela hash')
            elif opcao == '3':
                exit()
   
   
def trabalhador():
    usuario = input('Usúario: ')
    senha = input('Senha: ')
    print('''
   [ 1 ] Adicionar um produto  [ 1 ]
   [ 2 ]  Remover um produto   [ 2 ] 
   [ 3 ] Ver todos os produtos [ 3 ]
   [ 4 ]  Pesquisar pelo nome  [ 4 ]
   [ 5 ]        SAIR           [ 5 ]
''')
    opcao = input('Resposta: ')
    if opcao == '1':
        print('adicionar um produto na tabela hash')
    elif opcao == '2':
        print(' remover um produto da tabela hash')
    elif opcao == '3':
        print(' Ver todos os produtos da tabela hash')
    elif opcao == 4:
        print('Pesquisar pelo nome na tabela hash')
    elif opcao == 5:
        exit()
    else:
        while opcao not in '12345':        
            print('\033[1;31m OPÇÃO INVÁLIDA \033[m')
            opcao = input(' Qual sua resposta? ')
            if opcao == '1':
                print('adicionar um produto na tabela hash')
            elif opcao == '2':
                print(' remover um produto da tabela hash')
            elif opcao == '3':
                print(' Ver todos os produtos da tabela hash')
            elif opcao == 4:
                print('Pesquisar pelo nome na tabela hash')
            elif opcao == 5:
                exit()
 

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
    trabalhador()
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