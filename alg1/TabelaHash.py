class TabelaHash:
    def __init__(self, capacidade=10):
        self.capacidade = capacidade
        self.tabela = [[] for _ in range(capacidade)]
        self.size = 0

    def hash(self, chave):
        return hash(chave) % self.capacidade

    def inserir(self, chave, valor):
        indice = self.hash(chave)
        for par in self.tabela[indice]:
            if par[0] == chave:
                par[1] = valor
                return

        self.tabela[indice].append([chave, valor])
        self.size += 1

    def buscar(self, chave):
        indice = self.hash(chave)
        for par in self.tabela[indice]:
            return par[1]
        return None

    def remover(self, chave):
        indice = self.hash(chave)
        for i, par in enumerate(self.tabela[indice]):
            if par[0] == chave:
                del self.tabela[indice][i]
                self.size -= 1
                return True
        return False

    def __str__(self):
        resultado = []
        for lista in self.tabela:
            for par in lista:
                resultado.append(f"{par[0]}: {par[1]}")
        return "{ " + ", ".join(resultado) + " }"

