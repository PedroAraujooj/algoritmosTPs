import random
import time


class GrafoAlgoritmoPrim:
    def __init__(self):
        self.grafo = {}

    def adicionar_aresta(self, u, v, peso):
        if u not in self.grafo:
            self.grafo[u] = []
        if v not in self.grafo:
            self.grafo[v] = []
        self.grafo[u].append((v, peso))
        self.grafo[v].append((u, peso))

    def get_peso(self, u, v):
        for (vizinho, peso) in self.grafo[u]:
            if vizinho == v:
                return peso
        return float('inf')

    def prim(self, raiz):
        infinito = float('inf')
        vertices = list(self.grafo.keys())
        chave = {vertice: infinito for vertice in vertices}
        pai = {vertice: None for vertice in vertices}
        selecionado = {vertice: False for vertice in vertices}

        chave[raiz] = 0

        for _ in range(len(vertices)):
            u = min((v for v in vertices if not selecionado[v]),
                    key=lambda v: chave[v],
                    default=None)
            if u is None:
                break
            selecionado[u] = True

            for (vizinho, peso) in self.grafo[u]:
                if not selecionado[vizinho] and peso < chave[vizinho]:
                    chave[vizinho] = peso
                    pai[vizinho] = u

        return pai

    def imprimir(self, raiz):
        pai = self.prim(raiz)
        custo_total = 0

        print(f"\nArestas da Árvore Geradora Mínima (iniciando em {raiz}):")
        for vertice, pai_vertice in pai.items():
            if pai_vertice is not None:
                peso = self.get_peso(vertice, pai_vertice)
                print(f"{pai_vertice} - {vertice} (custo: {peso})")
                custo_total += peso
        print(f"Custo total da MST: {custo_total}")


if __name__ == "__main__":

    verticesAndArestas = {
        'A': [('B', 2), ('C', 3)],
        'B': [('A', 2), ('C', 1), ('D', 4)],
        'C': [('A', 3), ('B', 1), ('D', 5)],
        'D': [('B', 4), ('C', 5)]

    }
    grafoPqn = GrafoAlgoritmoPrim()
    grafoPqn.grafo = verticesAndArestas
    print("== Grafo Pequeno ==")
    grafoPqn.imprimir('A')
    inicio = time.time()
    for _ in range(1000):
        grafoPqn.prim('A')
    fim = time.time()
    print(f"Tempo de execução (grafo pequeno): {((fim - inicio) / 1000):.20f} segundos\n")

    grafo_grande = GrafoAlgoritmoPrim()
    cidades = [f"C{i}" for i in range(100)]
    for cidade in cidades:
        grafo_grande.grafo[cidade] = []
    num_arestas = 5 * 100
    for _ in range(num_arestas):
        u = random.choice(cidades)
        v = random.choice(cidades)
        if u != v:
            peso = random.randint(1, 1000)
            grafo_grande.adicionar_aresta(u, v, peso)

    print("== Grafo Grande ==")
    grafo_grande.imprimir('C0')
    inicio = time.time()
    for _ in range(1000):
        grafo_grande.prim('C0')
    fim = time.time()
    print(f"Tempo de execução (grafo grande): {((fim - inicio) / 1000):.20f} segundos\n")
