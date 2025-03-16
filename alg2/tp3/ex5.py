from alg2.tp3.GrafoPonderadoCidadeInteligente import GrafoPonderadoCidadeInt

if __name__ == "__main__":
    g = GrafoPonderadoCidadeInt()
    g.adicionar_cruzamento("A", recarga=True)
    g.adicionar_cruzamento("B")
    g.adicionar_cruzamento("C", recarga=True)
    g.adicionar_cruzamento("D")
    g.adicionar_cruzamento("E", recarga=True)
    g.adicionar_cruzamento("F")
    g.adicionar_aresta("A", "B", 5, 10)
    g.adicionar_aresta("B", "C", 2, 5)
    g.adicionar_aresta("B", "D", 8, 12)
    g.adicionar_aresta("C", "E", 5, 10)
    g.adicionar_aresta("D", "E", 3, 6)
    g.adicionar_aresta("E", "F", 7, 15)
    g.adicionar_aresta("B", "E", 9, 22)
    caminho, tempo = g.dijkstra("A", "F", 20)
    print(caminho, tempo)