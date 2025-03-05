from alg2.tp2.listaAdjacenciaDirecionada import GrafoDirecionado

if __name__ == "__main__":
    grafo = GrafoDirecionado()

    for node in [1, 2, 3, 4, 5, 6]:
        grafo.adicionar_vertice(node)

    grafo.lista_adjacencia = {
        1: [2, 3],
        2: [4],
        3: [5],
        4: [6],
        5: [6],
        6: []
    }

    ordem_bfs = grafo.bfs(1)
    print("Ordem BFS:", ordem_bfs)
    ordem_dfs = grafo.dfs(1)
    print("Ordem DFS:", ordem_dfs)
