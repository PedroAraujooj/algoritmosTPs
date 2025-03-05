from collections import deque


class GrafoComPesos:
    def __init__(self):
        self.lista_adjacencia = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.lista_adjacencia:
            self.lista_adjacencia[vertice] = []

    def adicionar_aresta(self, v1, v2, peso=1):
        if v1 in self.lista_adjacencia and v2 in self.lista_adjacencia:
            self.lista_adjacencia[v1].append((v2, peso))
            self.lista_adjacencia[v2].append((v1, peso))

    def mostrar_vizinhos(self, vertice):
        if vertice in self.lista_adjacencia:
            print(f"Vizinhos de {vertice}: {self.lista_adjacencia[vertice]}")
        else:
            print(f"O vértice {vertice} não existe no grafo.")

    def bfs(self, inicio, destino):
        visitados = set()
        fila = deque()
        pais = {}

        fila.append(inicio)
        visitados.add(inicio)
        pais[inicio] = None

        while fila:
            vertice_atual = fila.popleft()

            if vertice_atual == destino:
                break

            for adj in self.lista_adjacencia[vertice_atual]:
                vizinho = adj[0]
                if vizinho not in visitados:
                    visitados.add(vizinho)
                    pais[vizinho] = vertice_atual
                    fila.append(vizinho)

        caminho = []
        if destino in pais:
            vertice = destino
            while vertice is not None:
                caminho.append(vertice)
                vertice = pais[vertice]
            caminho.reverse()

        return caminho
