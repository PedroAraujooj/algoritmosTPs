from alg2.tp2.listaAdjacencia import Grafo

if __name__ == "__main__":
    grafo = Grafo()

    for centro in ["A", "B", "C", "D", "E"]:
        grafo.adicionar_vertice(centro)

    grafo.lista_adjacencia = {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A", "E"],
        "D": ["B"],
        "E": ["C"]
    }
    ordem_dfs = grafo.dfs("A")
    print("Ordem DFS:", ordem_dfs)
