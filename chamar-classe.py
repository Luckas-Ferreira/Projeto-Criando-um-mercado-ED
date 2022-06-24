#Os comandos para usar no SistemaLogistico.py


from TabelaHash import *

tamanhoHash = 2
tab = Hash(tamanhoHash)
print("\n****************************************************")
print("      Tabela HASH Sem Colisões (%d itens) " %tamanhoHash)
print("****************************************************")
for i in range (0,tamanhoHash,1):
     print("\nInserindo elemento %d" %(i + 1));
     item = input(" - Forneca valor numerico inteiro: ")
     tab.insere(item)
item = input("\n - Forneca valor numerico inteiro para buscar: ")
pos = tab.busca(item)
if pos == -1:
     print("Item nao encontrado")
else:
     print("Item encontrado na posicao: ", pos)
item = input("\n - Forneca valor numerico inteiro para apagar: ")
tab.apaga(item)
print("\nImprimindo conteudo")
tab.imprime()
print("\n")