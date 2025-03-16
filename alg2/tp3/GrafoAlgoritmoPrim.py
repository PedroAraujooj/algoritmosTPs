class GrafoAlgoritmoPrim:
    def __init__(self, vertices):
        self.V = vertices
        self.grafo = [[0] * vertices for _ in range(vertices)]

    def adicionar_aresta(self, u, v, peso):
        self.grafo[u][v] = peso
        self.grafo[v][u] = peso

    def prim(self):
        infinito = float('inf')
        selecionado = [False] * self.V
        chave = [infinito] * self.V
        pai = [-1] * self.V

        chave[0] = 0

        for _ in range(self.V):
            minimo = infinito
            u = -1
            for v in range(self.V):
                if not selecionado[v] and chave[v] < minimo:
                    minimo = chave[v]
                    u = v

            selecionado[u] = True

            for v in range(self.V):
                if 0 < self.grafo[u][v] < chave[v] and not selecionado[v]:
                    chave[v] = self.grafo[u][v]
                    pai[v] = u

        print("\nArestas da Árvore Geradora Mínima:")
        return pai

    def imprimir(self, pai):
        custo_total = 0
        for i in range(1, self.V):
            print(f"{pai[i]} - {i} (Peso: {self.grafo[i][pai[i]]})")
            custo_total += self.grafo[i][pai[i]]
        print(f"Peso total da AGM: {custo_total}")

    def imprimir_bairros(self, pai):
        custo_total = 0
        for i in range(1, self.V):
            print(f"Bairro {pai[i]} - Bairro {i} (Custo: R${self.grafo[i][pai[i]]})")
            custo_total += self.grafo[i][pai[i]]
        print(f"Custo total da instalação: R${custo_total}")

    def imprimir_cidades(self, pai):
        custo_total = 0
        for i in range(1, self.V):
            print(f"Cidade {pai[i]} - Cidade {i} (Custo: R${self.grafo[i][pai[i]]})")
            custo_total += self.grafo[i][pai[i]]
        print(f"Custo total para construir linhas de transmissão: R${custo_total}")

    def imprimir_abastecimento_agua(self, pai):
        custo_total = 0
        for i in range(1, self.V):
            print(f"Cidade {pai[i]} - Cidade {i} (Custo: R${self.grafo[i][pai[i]]})")
            custo_total += self.grafo[i][pai[i]]
        print(f"Custo total de instalação de tubulações: R${custo_total}")

    def imprimir_torres(self, pai):
        custo_total = 0
        for i in range(1, self.V):
            print(f"Região {pai[i]} - Região {i} (Custo: R${self.grafo[i][pai[i]]})")
            custo_total += self.grafo[i][pai[i]]
        print(f"Custo total para construir torres de comunicação: R${custo_total}")