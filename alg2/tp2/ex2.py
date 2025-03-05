from alg2.tp2.listaAdjacencia import Grafo

if __name__ == "__main__":
    grafo = Grafo()

    for v in ["Agua Santa", "Encantado", "Quintino", "Meier", "Campinho", "Cascadura"]:
        grafo.adicionar_vertice(v)

    arestas = [("Agua Santa", "Quintino"), ("Agua Santa", "Encantado"), ("Encantado", "Quintino"), ("Encantado", "Meier"),
               ("Quintino", "Campinho"), ("Quintino", "Cascadura"), ("Campinho", "Cascadura")]
    for v1, v2 in arestas:
        grafo.adicionar_aresta(v1, v2)

    print("Lista de Adjacência do Grafo:")
    grafo.mostrar_grafo()
