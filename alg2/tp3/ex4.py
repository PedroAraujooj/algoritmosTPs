from alg2.tp3.GrafoPonderado import GrafoPoderado

if __name__ == "__main__":
    mapa_cidades = GrafoPoderado()
    cidades = ["A", "B", "C", "D", "E", "F", "G"]

    for cidade in cidades:
        mapa_cidades.adicionar_vertice(cidade)

    custos = [
        ("A", "B", 200), ("A", "C", 150),
        ("B", "C", 250), ("B", "D", 100),
        ("C", "E", 350), ("D", "E", 300),
        ("D", "F", 250), ("E", "F", 100),
        ("F", "G", 150)
    ]

    for b1, b2, c in custos:
        mapa_cidades.adicionar_arestas(b1, b2, c)

    origem = "A"
    destino = "F"
    rota, custo = mapa_cidades.dijkstra(origem, destino)

    print(f"\nMelhor rota da cidade {origem} para  a cidade {destino}: {' => '.join(rota)}")
    print(f"Custo total: R${custo} ")