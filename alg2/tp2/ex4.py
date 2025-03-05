from alg2.tp2.listaAdjacencia import Grafo

if __name__ == "__main__":
    grafo = Grafo()

    for v in ["Centro", "A", "B", "C", "D"]:
        grafo.adicionar_vertice(v)

    arestas = [("Centro", "A"), ("Centro", "B"), ("A", "C"), ("B", "C"),
               ("C", "D")]
    for v1, v2 in arestas:
        grafo.adicionar_aresta(v1, v2)

    print("Lista de Adjacência do Grafo:")
    grafo.mostrar_grafo()

    grafo.mostrar_vizinhos("Centro")
