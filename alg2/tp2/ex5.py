from alg2.tp2.listaAdjacenciaComPeso import GrafoComPesos

if __name__ == "__main__":
    grafo = GrafoComPesos()

    for centro in ["A", "B", "C", "D", "E"]:
        grafo.adicionar_vertice(centro)

    arestas = [("A", "B", 1), ("A", "C", 2), ("B", "D", 3), ("C", "E", 4), ("D", "E", 5)]
    for v1, v2, p in arestas:
        grafo.adicionar_aresta(v1, v2, p)

    for centro in grafo.lista_adjacencia:
        grafo.mostrar_vizinhos(centro)

    caminho = grafo.bfs("A", "E")
    print("Rota encontrada (BFS):", caminho)