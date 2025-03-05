from alg2.tp2.listaAdjacencia import Grafo

if __name__ == "__main__":
    grafo = Grafo()

    for centro in ["A", "B", "C", "D", "E", "F"]:
        grafo.adicionar_vertice(centro)

    grafo.lista_adjacencia = {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A", "E"],
        "D": ["B", "F"],
        "E": ["C", "F"],
        "F": ["D", "E"]
    }

    print(grafo.bfs("A"))
