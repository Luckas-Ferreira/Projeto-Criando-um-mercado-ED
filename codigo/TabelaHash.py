import random
from time import sleep

class cor:
  def __init__(self):
    self.cor = None
  def close(cor= None):
    close = '\033[m'
    return close
  def red(cor = None):
      red = '\033[1;31m'
      return red
  def green(cor = None):
    blue = '\033[1;32m'
    return blue
  def yellow(cor = None):
    yellow = '\033[1;33m'
    return yellow

class  TabelaHash:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self,key,data):
      hashvalue = self.hashfunction(key,len(self.slots))

      if self.slots[hashvalue] == None:
        self.slots[hashvalue] = key
        self.data[hashvalue] = data
      else:
        if self.slots[hashvalue] == key:
          self.data[hashvalue] = data  #replace
        else:
          nextslot = self.rehash(hashvalue,len(self.slots))
          while self.slots[nextslot] != None and \
                          self.slots[nextslot] != key:
            nextslot = self.rehash(nextslot,len(self.slots))

          if self.slots[nextslot] == None:
            self.slots[nextslot]=key
            self.data[nextslot]=data
          else:
            self.data[nextslot] = data #replace

    def hashfunction(self,key,size):
         return key%size

    def rehash(self,oldhash,size):
        return (oldhash+1)%size

    def get(self,key):
      startslot = self.hashfunction(key,len(self.slots))

      data = None
      stop = False
      found = False
      position = startslot
      while self.slots[position] != None and  \
                           not found and not stop:
         if self.slots[position] == key:
           found = True
           data = self.data[position]
         else:
           position=self.rehash(position,len(self.slots))
           if position == startslot:
               stop = True
      return data

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key,data)


Tabela = TabelaHash()
Tabela[1]=cor.green() + 'PLACA MÃE ------- R$500,00' + cor.close()
Tabela[26]=cor.green() + 'MEMORIA RAM ------ R$200,00' + cor.close()
Tabela[93]=cor.green() + 'PROCESSADOR I5 --- R$500,00' + cor.close()
Tabela[77]=cor.green() + 'SSD 256GB -------- R$200,00' + cor.close()
Tabela[31]=cor.green() + 'PLACA DE VÍDEO --- R$1500,00' + cor.close()
Tabela[44]=cor.green() + 'COOLER ----------- R$50,00' + cor.close()
Tabela[55]=cor.green() + 'GABINETE --------- R$300,00' + cor.close()
Tabela[20]=cor.green() + 'MONITOR ---------- R$400,00' + cor.close()


def mostrarProdutos():
  sleep(0.5)
  print(cor.yellow() + '\n  MOSTRANDO TODOS OS PRODUTOS \n' + cor.close())
  sleep(0.3)
  for k, v in enumerate(Tabela.data):
    if v == None:
      v = '\033[1;31mVazio ------------ R$0,00\033[m'
    print(k, v)
    sleep(0.1)



def adicionarProduto(produto):
  for posição in range(len(Tabela.slots)):
    if Tabela.slots[posição] is None:
      nome = input(cor.red() + 'Adicionar: ' + cor.close()).upper().strip()
      produto[nome] = random.randint(1, 100)
      for c in produto.values():
        posição = c
      valor = float(input(cor.red() + 'Valor: R$' + cor.close()))
      adicionar = (f'{nome} ---------- R${valor :.2f}')
      Tabela.put(posição,cor.green() + adicionar + cor.close())
      sleep(0.5)
      mostrarProdutos()
      sleep(0.5)
      return produto[nome]
  else:
    print(cor.red() + 'TABELA HASH ESTÁ CHEIA' + cor.close())


def pesquisarNome(produto2):
  pesquisa = str(input(cor.green() + 'Pesquisar: ' + cor.close())).upper().strip()
  produto1 = {'PLACA MÃE': 54, 'MEMORIA RAM': 26, 'PROCESSADOR': 93, 'SSD 256GB':77, 'PLACA DE VÍDEO':31, 'COOLER':44, 'GABINETE': 55, 'MONITOR': 20}
  produto1.update(produto2)
  novoProdutos = produto1
  for chave in novoProdutos.keys():
    if pesquisa == chave:
      valor_produto = novoProdutos[chave]
      for c in range(len(Tabela.slots)):
        if valor_produto == Tabela.slots[c]:
          sleep(0.5)
          print(cor.red() + '\n\n  ENCONTRAMOS SEU PRODUTO \n' + cor.close())
          sleep(0.5)
          item = Tabela.get(valor_produto)
          return print(item)
  else:
    print(cor.red() + '\n\n  NÃO TEMOS ESTE PRODUTO \n' + cor.close())
