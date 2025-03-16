from alg2.tp3.GrafoAlgoritmoPrim import GrafoAlgoritmoPrim

if __name__ == "__main__":
    g = GrafoAlgoritmoPrim(6)

    arestas = [
        (0, 1, 160000), (0, 2, 80000), (1, 2, 200000),
        (1, 3, 400000), (2, 3, 320000), (2, 4, 120000),
        (3, 4, 280000), (3, 5, 240000), (4, 5, 40000)
    ]

    for u, v, peso in arestas:
        g.adicionar_aresta(u, v, peso)

    resultado = g.prim()
    g.imprimir_torres(resultado)