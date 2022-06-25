from optparse import Values


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
Tabela[54]='Placa Mãe ------- R$'
Tabela[26]='Memoria RAM ------ R$'
Tabela[93]='Processador I5 --- R$'
Tabela[17]='SSD 500GB -------- R$'
Tabela[77]='SSD 256GB -------- R$'
Tabela[31]='Placa Nvidia ----- R$'
Tabela[44]='Cooler ----------- R$'
Tabela[55]='Gabinete --------- R$'
Tabela[20]='Monitor ---------- R$'

print('Mostrando todos os produtos')
for k, v in enumerate(Tabela.data):
  if v == None:
    v = '\033[1;31mVazio ------------ R$0,00\033[m'
  print(k, v)
