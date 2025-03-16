from alg2.tp3.GrafoAlgoritmoPrim import GrafoAlgoritmoPrim

if __name__ == "__main__":
    g = GrafoAlgoritmoPrim(6)

    arestas = [
        (0, 1, 320000), (0, 2, 160000), (1, 2, 400000),
        (1, 3, 800000), (2, 3, 640000), (2, 4, 240000),
        (3, 4, 560000), (3, 5, 480000), (4, 5, 80000)
    ]

    for u, v, peso in arestas:
        g.adicionar_aresta(u, v, peso)

    resultado = g.prim()
    g.imprimir_abastecimento_agua(resultado)