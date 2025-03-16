from alg2.tp3.GrafoPonderado import GrafoPoderado

if __name__ == "__main__":
    mapa_cidades = GrafoPoderado()
    bairros = ["A", "B", "C", "D", "E", "F", "G"]

    for bairro in bairros:
        mapa_cidades.adicionar_vertice(bairro)

    estradas = [
        ("A", "B", 4), ("A", "C", 3),
        ("B", "C", 5), ("B", "D", 2),
        ("C", "E", 7), ("D", "E", 6),
        ("D", "F", 5), ("E", "F", 2),
        ("F", "G", 3)
    ]

    for b1, b2, distancia in estradas:
        mapa_cidades.adicionar_arestas(b1, b2, distancia)

    origem = "A"
    destino = "F"
    rota, distancia = mapa_cidades.dijkstra(origem, destino)

    print(f"\nMelhor rota de {origem} para {destino}: {' => '.join(rota)}")
    print(f"Distância total: {distancia} km")