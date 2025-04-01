from collections import deque


class Grafo:
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

    def mostrar_grafo(self):
        for vertice in self.lista_adjacencia:
            print(f"{vertice} -> {self.lista_adjacencia[vertice]}")

    def _dfs_ciclo(self, vertice, visitados, rec_stack):
        visitados.add(vertice)
        rec_stack.add(vertice)
        for (vizinho, _) in self.lista_adjacencia[vertice]:
            if vizinho not in visitados:
                if self._dfs_ciclo(vizinho, visitados, rec_stack):
                    return True
            elif vizinho in rec_stack:
                return True
        rec_stack.remove(vertice)
        return False

    def existe_ciclo(self):
        visitados = set()
        rec_stack = set()
        for vertice in self.lista_adjacencia:
            if vertice not in visitados:
                if self._dfs_ciclo(vertice, visitados, rec_stack):
                    return True
        return False

    def bfs_menor_distancia(self, inicio, destino):
        visitados = set()
        fila = deque()
        pais = {}
        fila.append(inicio)
        visitados.add(inicio)
        pais[inicio] = None
        while fila:
            atual = fila.popleft()
            if atual == destino:
                break
            for (vizinho, _) in self.lista_adjacencia[atual]:
                if vizinho not in visitados:
                    visitados.add(vizinho)
                    pais[vizinho] = atual
                    fila.append(vizinho)
        caminho = []
        if destino in pais:
            v = destino
            while v is not None:
                caminho.append(v)
                v = pais[v]
            caminho.reverse()
        return caminho

    def bfs(self, inicio):
        visitados = set()
        fila = deque()
        ordem = []
        fila.append(inicio)
        visitados.add(inicio)
        while fila:
            atual = fila.popleft()
            ordem.append(atual)
            for (vizinho, _) in self.lista_adjacencia[atual]:
                if vizinho not in visitados:
                    visitados.add(vizinho)
                    fila.append(vizinho)
        return ordem

    def dfs(self, inicio, visitados=None, ordem=None):
        if visitados is None:
            visitados = set()
        if ordem is None:
            ordem = []
        visitados.add(inicio)
        ordem.append(inicio)
        for (vizinho, _) in self.lista_adjacencia[inicio]:
            if vizinho not in visitados:
                self.dfs(vizinho, visitados, ordem)
        return ordem


class GrafoMatriz:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.matriz = [[0] * num_vertices for _ in range(num_vertices)]
        self.vertices = {}
        self.indice_para_vertice = {}
        self.contador = 0

    def adicionar_vertice(self, vertice):
        if vertice not in self.vertices and self.contador < self.num_vertices:
            self.vertices[vertice] = self.contador
            self.indice_para_vertice[self.contador] = vertice
            self.contador += 1

    def adicionar_aresta(self, v1, v2, peso=1):
        if v1 in self.vertices and v2 in self.vertices:
            i, j = self.vertices[v1], self.vertices[v2]
            self.matriz[i][j] = peso
            self.matriz[j][i] = peso

    def mostrar_matriz(self):
        print("Matriz de Adjacência:")
        print("  ", "  ".join(self.vertices.keys()))
        for i, linha in enumerate(self.matriz):
            print(self.indice_para_vertice[i], linha)

    def mostrar_vizinhos(self, vertice):
        if vertice in self.vertices:
            i = self.vertices[vertice]
            v = []
            for c in range(self.num_vertices):
                if self.matriz[i][c] != 0:
                    v.append((self.indice_para_vertice[c], self.matriz[i][c]))
            print(f"Vizinhos de {vertice}: {v}")
        else:
            print(f"O vértice {vertice} não existe no grafo.")


if __name__ == "__main__":
    g = Grafo()
    for vert in ["A", "B", "C", "D", "E", "F"]:
        g.adicionar_vertice(vert)
    g.lista_adjacencia = {
        "A": [("B", 4), ("C", 2)],
        "B": [("A", 4), ("D", 5)],
        "C": [("A", 2), ("D", 8), ("E", 3)],
        "D": [("B", 5), ("C", 8), ("F", 6)],
        "E": [("C", 3), ("F", 1)],
        "F": [("D", 6), ("E", 1)]
    }
    print("Lista de Adjacência:")
    g.mostrar_grafo()

    gm = GrafoMatriz(6)
    for v in ["A", "B", "C", "D", "E", "F"]:
        gm.adicionar_vertice(v)
    edges = [
        ("A", "B", 4), ("A", "C", 2),
        ("B", "A", 4), ("B", "D", 5),
        ("C", "A", 2), ("C", "D", 8), ("C", "E", 3),
        ("D", "B", 5), ("D", "C", 8), ("D", "F", 6),
        ("E", "C", 3), ("E", "F", 1),
        ("F", "D", 6), ("F", "E", 1)
    ]
    for v1, v2, p in edges:
        gm.adicionar_aresta(v1, v2, p)
    gm.mostrar_matriz()
