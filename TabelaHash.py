class Hash:

     def __init__(self,tam):
          self.tab = {}
          self.tam_max = tam

     def funcaohash(self, chave):
          v = int(chave)
          return v%self.tam_max

     def cheia(self):
          return len(self.tab) == self.tam_max

     def imprime(self):
          for i in self.tab:
               print("Hash[%d] = " %i, end="")
               print (self.tab[i])

     def apaga(self, chave):
          pos = self.busca(chave)
          if pos != -1:
               del self.tab[pos]
               print("-> Dado da posicao %d apagado" %pos) 
          else:
               print("Item nao encontrado")

     def busca(self, chave):
          pos = self.funcaohash(chave)
          if self.tab.get(pos) == None: # se esta posição não existe
               return -1 #saida imediata
          if self.tab[pos] == chave: 
               return pos
          return -1

     def insere(self, item):
          if self.cheia():
               print("-> ATENÇÃO Tabela Hash CHEIA")
               return
          pos = self.funcaohash(str(item))
          print("Posição recebida inicialmente: "+ str(pos))
          if self.tab.get(pos) == None: # se posicao vazia
               self.tab[pos] = str(item)
               print("-> Inserido HASH[%d]" %pos)          
          else: # se posicao ocupada, insere na próxima disponível
            print(" - Posição ocupada")
            newPos = int(self.tab[pos]) + 1
            while self.tab.get(newPos) != None:
                newPos += 1
                
            self.tab[newPos] = str(item)          
            print("-> Inserido HASH[%d]" %newPos)            
# fim Classe Hashlinear