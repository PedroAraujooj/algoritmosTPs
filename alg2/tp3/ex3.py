from alg2.tp3.GrafoPonderado import GrafoPoderado

if __name__ == "__main__":
    mapa_aeroportos = GrafoPoderado()
    aeroportos = ["A", "B", "C", "D", "E", "F", "G"]

    for aeroporto in aeroportos:
        mapa_aeroportos.adicionar_vertice(aeroporto)

    distancias = [
        ("A", "B", 800), ("A", "C", 600),
        ("B", "C", 1000), ("B", "D", 400),
        ("C", "E", 1400), ("D", "E", 1200),
        ("D", "F", 1000), ("E", "F", 400),
        ("F", "G", 600)
    ]

    for b1, b2, t in distancias:
        mapa_aeroportos.adicionar_arestas(b1, b2, t)

    origem = "A"
    destino = "F"
    rota, distancia = mapa_aeroportos.dijkstra(origem, destino)

    print(f"\nMelhor rota do aeroporto {origem} para  o aeroporto {destino}: {' => '.join(rota)}")
    print(f"Distância total: {distancia} km")