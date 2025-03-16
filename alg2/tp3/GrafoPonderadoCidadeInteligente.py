import heapq


class Cruzamento:
    def __init__(self, nome, recarga=False):
        self.nome = nome
        self.recarga = recarga
        self.arestas = []


class Aresta:
    def __init__(self, destino, tempo, distancia):
        self.destino = destino
        self.tempo = tempo
        self.distancia = distancia


class GrafoPonderadoCidadeInt:
    def __init__(self):
        self.cruzamentos = {}

    def adicionar_cruzamento(self, nome, recarga=False):
        if nome not in self.cruzamentos:
            self.cruzamentos[nome] = Cruzamento(nome, recarga)

    def adicionar_aresta(self, origem, destino, tempo, distancia):

        self.adicionar_cruzamento(origem)
        self.adicionar_cruzamento(destino)

        cruz_orig = self.cruzamentos[origem]
        cruz_dest = self.cruzamentos[destino]

        cruz_orig.arestas.append(Aresta(cruz_dest, tempo, distancia))
        cruz_dest.arestas.append(Aresta(cruz_orig, tempo, distancia))

    def dijkstra(self, origem, destino, autonomia):
        dist = {nome: float("inf") for nome in self.cruzamentos}
        dist[origem] = 0
        predecessor = {}
        nao_visitados = set(self.cruzamentos.keys())

        while nao_visitados:
            atual = min(nao_visitados, key=lambda v: dist[v])
            nao_visitados.remove(atual)
            if dist[atual] == float("inf"):
                break
            if atual == destino:
                break
            for aresta in self.cruzamentos[atual].arestas:
                if aresta.distancia <= autonomia or self.cruzamentos[atual].recarga:
                    novo_tempo = dist[atual] + aresta.tempo
                    if novo_tempo < dist[aresta.destino.nome]:
                        dist[aresta.destino.nome] = novo_tempo
                        predecessor[aresta.destino.nome] = atual
        if dist[destino] == float("inf"):
            return None, float("inf")
        caminho = []
        v = destino
        while v in predecessor:
            caminho.append(v)
            v = predecessor[v]
        caminho.append(origem)
        caminho.reverse()
        return caminho, dist[destino]
