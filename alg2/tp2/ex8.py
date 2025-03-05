from alg2.tp2.listaAdjacencia import Grafo

if __name__ == "__main__":
    grafo = Grafo()

    for centro in ["A", "B", "C", "D", "X", "Y"]:
        grafo.adicionar_vertice(centro)

    arestas = [("A", "B"),
               ("B", "C"),
               ("C", "D"),
               ("D", "A"),
               ("A", "X"),
               ("X", "Y")]
    for v1, v2 in arestas:
        grafo.adicionar_aresta(v1, v2)

    if grafo.existe_ciclo():
        print("Há um ciclo suspeito no grafo de transações.")
    else:
        print("Não foi detectado nenhum ciclo suspeito.")