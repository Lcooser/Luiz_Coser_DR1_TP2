class TabelaHash:
    def __init__(self, tamanho=10):
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]

    def _hash(self, chave):
        return hash(chave) % self.tamanho

    def inserir(self, chave, valor):
        indice = self._hash(chave)
        for i, (k, v) in enumerate(self.tabela[indice]):
            if k == chave:
                self.tabela[indice][i] = (chave, valor)
                return
        self.tabela[indice].append((chave, valor))

    def buscar(self, chave):
        indice = self._hash(chave)
        for k, v in self.tabela[indice]:
            if k == chave:
                return v
        return None

    def remover(self, chave):
        indice = self._hash(chave)
        for i, (k, v) in enumerate(self.tabela[indice]):
            if k == chave:
                del self.tabela[indice][i]

tabela = TabelaHash()

tabela.inserir("nome", "Flavio")
tabela.inserir("idade", 30)
tabela.inserir("cidade", "Olinda")

print(tabela.buscar("nome")) 
print(tabela.buscar("idade"))
print(tabela.buscar("cidade"))

tabela.remover("idade")
print(tabela.buscar("idade"))  
