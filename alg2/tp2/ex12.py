from alg2.tp2.listaAdjacencia import Grafo

if __name__ == "__main__":
    cidade = Grafo()

    for bairro in ["A", "B", "C", "D", "E", "F"]:
        cidade.adicionar_vertice(bairro)

    arestas = [
        ("A", "B"),
        ("A", "C"),
        ("B", "D"),
        ("B", "E"),
        ("C", "D"),
        ("D", "E"),
        ("D", "F"),
        ("E", "F")
    ]
    for v1, v2 in arestas:
        cidade.adicionar_aresta(v1, v2)
    caminho_curto = cidade.bfs_menor_distancia("A", "F")
    print("\nCaminho mais curto de A até F:", " -> ".join(caminho_curto))
