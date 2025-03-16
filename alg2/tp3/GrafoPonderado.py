class GrafoPoderado:
    def __init__(self):
        self.vertices = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = {}

    def adicionar_arestas(self, vertice1, vertice2, peso):
        self.vertices[vertice1][vertice2] = peso
        self.vertices[vertice2][vertice1] = peso

    def dijkstra(self, origem, destino):
        nao_visitados = list(self.vertices.keys())
        pesos = {vertice: float("inf") for vertice in self.vertices}
        pesos[origem] = 0
        predecessores = {}


        while nao_visitados:
            vertice_atual = min(nao_visitados, key=lambda vertice: pesos[vertice])

            if pesos[vertice_atual] == float("inf"):
                break

            for vizinho, peso in self.vertices[vertice_atual].items():
                novo_peso = pesos[vertice_atual] + peso
                if novo_peso < pesos[vizinho]:
                    pesos[vizinho] = novo_peso
                    predecessores[vizinho] = vertice_atual

            nao_visitados.remove(vertice_atual)

        caminho = []
        verice_atual = destino
        while verice_atual in predecessores:
            caminho.append(verice_atual)
            verice_atual = predecessores[verice_atual]
        caminho.append(origem)
        caminho.reverse()

        return caminho, pesos[destino]