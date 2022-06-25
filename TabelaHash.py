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
Tabela[54]=cor.green() + 'Placa Mãe ------- R$' + cor.close()
Tabela[26]=cor.green() + 'Memoria RAM ------ R$' + cor.close()
Tabela[93]=cor.green() + 'Processador I5 --- R$' + cor.close()
Tabela[17]=cor.green() + 'SSD 500GB -------- R$' + cor.close()
Tabela[77]=cor.green() + 'SSD 256GB -------- R$' + cor.close()
Tabela[31]=cor.green() + 'Placa Nvidia ----- R$' + cor.close()
Tabela[44]=cor.green() + 'Cooler ----------- R$' + cor.close()
Tabela[55]=cor.green() + 'Gabinete --------- R$' + cor.close()
Tabela[20]=cor.green() + 'Monitor ---------- R$' + cor.close()

def mostrarProdutos():
  print('Mostrando todos os produtos')
  for k, v in enumerate(Tabela.data):
    if v == None:
      v = '\033[1;31mVazio ------------ R$0,00\033[m'
    print(k, v)

def pesquisarNome():
  item = Tabela.get(int(input('Pesquisar: ')))
  return item

print(pesquisarNome())