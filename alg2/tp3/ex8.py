INF = float('inf')


def floyd_warshall(grafo):
    num_vertices = len(grafo)

    dist = [[grafo[i][j] for j in range(num_vertices)] for i in range(num_vertices)]

    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


if __name__ == "__main__":

    grafo_cidades = [
        [0, 3, INF, 7, INF],
        [3, 0, 2, INF, INF],
        [INF, 2, 0, 5, 1],
        [7, INF, 5, 0, 2],
        [INF, INF, 1, 2, 0]
    ]

    menores_caminhos = floyd_warshall(grafo_cidades)

    print("Matriz das menores distâncias entre todas as cidades(em KM):")
    for i, linha in enumerate(menores_caminhos):
        print(f"Cidade {i + 1}: {linha}")
