from alg2.tp3.GrafoAlgoritmoPrim import GrafoAlgoritmoPrim

if __name__ == "__main__":
    g = GrafoAlgoritmoPrim(6)

    arestas = [
        (0, 1, 8000), (0, 2, 4000), (1, 2, 10000),
        (1, 3, 20000), (2, 3, 16000), (2, 4, 6000),
        (3, 4, 14000), (3, 5, 12000), (4, 5, 2000)
    ]

    for u, v, peso in arestas:
        g.adicionar_aresta(u, v, peso)

    resultado = g.prim()
    g.imprimir_cidades(resultado)