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
grafo_cidades = [
    [0, 5, 10, INF, INF, INF],   # Cidade A
    [5, 0, 3, 8, INF, INF],   # Cidade B
    [10, 3, 0, 2, 7, INF],   # Cidade C
    [INF, 8, 2, 0, 4, 6],   # Cidade D
    [INF, INF, 7, 4, 0, 5],   # Cidade E
    [INF, INF, INF, 6, 5, 0],   # Cidade F
]

menores_caminhos = floyd_warshall(grafo_cidades)

print("Matriz das menores distâncias entre todas as cidades:")
for linha in menores_caminhos:
    print(linha)
