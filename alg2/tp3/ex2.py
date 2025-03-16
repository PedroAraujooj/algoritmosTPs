from alg2.tp3.GrafoPonderado import GrafoPoderado

if __name__ == "__main__":
    mapa_cidades = GrafoPoderado()
    bairros = ["A", "B", "C", "D", "E", "F", "G"]

    for bairro in bairros:
        mapa_cidades.adicionar_vertice(bairro)

    tempos = [
        ("A", "B", 8), ("A", "C", 6),
        ("B", "C", 10), ("B", "D", 4),
        ("C", "E", 14), ("D", "E", 12),
        ("D", "F", 10), ("E", "F", 4),
        ("F", "G", 6)
    ]

    for b1, b2, t in tempos:
        mapa_cidades.adicionar_arestas(b1, b2, t)

    origem = "A"
    destino = "F"
    rota, tempo = mapa_cidades.dijkstra(origem, destino)

    print(f"\nMelhor rota de {origem} para {destino}: {' => '.join(rota)}")
    print(f"Tempo total: {tempo} minutos")