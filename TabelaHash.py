import random

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

class  TabelaHash:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def adcionar(self,key,data):
      valorHash = self.funcaoHash(key,len(self.slots))

      if self.slots[valorHash] == None:
        self.slots[valorHash] = key
        self.data[valorHash] = data
      else:
        if self.slots[valorHash] == key:
          self.data[valorHash] = data  #replace
        else:
          nextslot = self.refazer(valorHash,len(self.slots))
          while self.slots[nextslot] != None and \
                          self.slots[nextslot] != key:
            nextslot = self.refazer(nextslot,len(self.slots))

          if self.slots[nextslot] == None:
            self.slots[nextslot]=key
            self.data[nextslot]=data
          else:
            self.data[nextslot] = data #replace

    def funcaoHash(self,key,size):
         return key%size

    def refazer(self,oldhash,size):
        return (oldhash+1)%size

    def get(self,key):
      startslot = self.funcaoHash(key,len(self.slots))

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
           position=self.refazer(position,len(self.slots))
           if position == startslot:
               stop = True
      return data

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.adcionar(key,data)


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
  print('Mostrando todos os produtos')
  for k, v in enumerate(Tabela.data):
    if v == None:
      v = '\033[1;31mVazio ------------ R$0,00\033[m'
    print(k, v)



def adicionarProduto(produto):
  for posição in range(len(Tabela.slots)):
    if Tabela.slots[posição] is None:
      nome = input('Adicionar: ').upper()
      produto[nome] = random.randint(1, 100)
      for c in produto.values():
        posição = c
      valor = float(input('Valor: R$'))
      adicionar = (f'{nome} ---------- R${valor :.2f}')
      Tabela.put(posição,cor.green() + adicionar + cor.close())
      mostrarProdutos()
      return produto[nome]
  else:
    print(cor.red() + 'TABELA HASH ESTÁ CHEIA' + cor.close())


def pesquisarNome(produto2):
  pesquisa = str(input('Pesquisar: ')).upper()
  produto1 = {'PLACA MÃE': 54, 'MEMORIA RAM': 26, 'PROCESSADOR': 93, 'SSD 256GB':77, 'PLACA DE VÍDEO':31, 'COOLER':44, 'GABINETE': 55, 'MONITOR': 20}
  produto1.update(produto2)
  novoProdutos = produto1
  for chave in novoProdutos.keys():
    if pesquisa == chave:
      valor_produto = novoProdutos[chave]
      for c in range(len(Tabela.slots)):
        if valor_produto == Tabela.slots[c]:
          print(Tabela.slots[c])
          print('Escontramos seu produto!')
          item = Tabela.get(valor_produto)
          return print(item)
  else:
    print('Não temos esse produto!')
