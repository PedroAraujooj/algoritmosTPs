from alg2.tp3.GrafoAlgoritmoPrim import GrafoAlgoritmoPrim

if __name__ == "__main__":
    g = GrafoAlgoritmoPrim(6)

    arestas = [
        (0, 1, 400), (0, 2, 200), (1, 2, 500),
        (1, 3, 1000), (2, 3, 800), (2, 4, 300),
        (3, 4, 700), (3, 5, 600), (4, 5, 100)
    ]

    for u, v, peso in arestas:
        g.adicionar_aresta(u, v, peso)

    resultado = g.prim()
    g.imprimir_bairros(resultado)