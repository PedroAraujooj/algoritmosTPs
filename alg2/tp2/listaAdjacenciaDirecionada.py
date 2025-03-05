from collections import deque


class GrafoDirecionado:
    def __init__(self):
        self.lista_adjacencia = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.lista_adjacencia:
            self.lista_adjacencia[vertice] = []


    def adicionar_aresta(self, vertice1, vertice2):
        if vertice1 in self.lista_adjacencia and vertice2 in self.lista_adjacencia:
            self.lista_adjacencia[vertice1].append(vertice2)


    def mostrar_vizinhos(self, vertice):
        if vertice in self.lista_adjacencia:
            print(f"Vizinhos de {vertice}: {self.lista_adjacencia[vertice]}")
        else:
            print(f"O vértice {vertice} não existe no grafo.")

    def mostrar_grafo(self):
        for vertice in self.lista_adjacencia:
            print(f"{vertice} -> {self.lista_adjacencia[vertice]}")


    def bfs(self, inicio):
        visitados = set()
        fila = deque()
        ordem_visita = []

        fila.append(inicio)
        visitados.add(inicio)

        while fila:
            vertice_atual = fila.popleft()
            ordem_visita.append(vertice_atual)
            for vizinho in self.lista_adjacencia[vertice_atual]:
                if vizinho not in visitados:
                    visitados.add(vizinho)
                    fila.append(vizinho)

        return ordem_visita

    def dfs(self, inicio, visitados=None, ordem_visita=None):
        if visitados is None:
            visitados = set()
        if ordem_visita is None:
            ordem_visita = []

        visitados.add(inicio)
        ordem_visita.append(inicio)

        for vizinho in self.lista_adjacencia[inicio]:
            if vizinho not in visitados:
                self.dfs(vizinho, visitados, ordem_visita)

        return ordem_visita