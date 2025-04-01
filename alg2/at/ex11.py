import random
import time

movimentos = [
    (2, 1), (2, -1), (-2, 1), (-2, -1),
    (1, 2), (1, -2), (-1, 2), (-1, -2)
]


def dentro_tabuleiro(x, y, N):
    return 0 <= x < N and 0 <= y < N


def movimentos_possiveis(tabuleiro, x, y, N):
    moves = []
    for dx, dy in movimentos:
        nx, ny = x + dx, y + dy
        if dentro_tabuleiro(nx, ny, N) and tabuleiro[nx][ny] == -1:
            moves.append((nx, ny))
    return moves


def proximo_movimento(tabuleiro, x, y, N):
    moves = movimentos_possiveis(tabuleiro, x, y, N)
    if not moves:
        return None
    moves.sort(key=lambda move: len(movimentos_possiveis(tabuleiro, move[0], move[1], N)))
    return moves[0]


def passeio_do_cavalo_warnsdorff(N, inicio_x=0, inicio_y=0):
    tabuleiro = [[-1] * N for _ in range(N)]
    x, y = inicio_x, inicio_y
    tabuleiro[x][y] = 0

    for i in range(1, N * N):
        prox = proximo_movimento(tabuleiro, x, y, N)
        if not prox:
            return None
        x, y = prox
        tabuleiro[x][y] = i

    return tabuleiro


def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(f"{num:2}" for num in linha))

def passeio_do_cavalo_forca_bruta(N, inicio_x=0, inicio_y=0):

    tabuleiro = [[-1] * N for _ in range(N)]
    tabuleiro[inicio_x][inicio_y] = 0

    if backtrack(tabuleiro, inicio_x, inicio_y, 1, N):
        return tabuleiro
    else:
        return None


def backtrack(tabuleiro, x, y, passo, N):
    if passo == N * N:
        return True

    for dx, dy in movimentos:
        nx, ny = x + dx, y + dy
        if dentro_tabuleiro(nx, ny, N) and tabuleiro[nx][ny] == -1:
            tabuleiro[nx][ny] = passo

            if backtrack(tabuleiro, nx, ny, passo + 1, N):
                return True

            tabuleiro[nx][ny] = -1

    return False


if __name__ == "__main__":

    print("=== Passeio do Cavalo (Warnsdorff) ===")
    print("5x5: ")
    inicio = time.time()
    solucao_warnsdorff5 = passeio_do_cavalo_warnsdorff(5)
    fim = time.time()
    imprimir_tabuleiro(solucao_warnsdorff5)
    print(f"Tempo para 5x5: {fim - inicio:.20f} segundos\n")

    print("8x8: ")
    inicio = time.time()
    solucao_warnsdorff8 = passeio_do_cavalo_warnsdorff(8)
    fim = time.time()
    imprimir_tabuleiro(solucao_warnsdorff8)
    print(f"Tempo para 8x8: {fim - inicio:.20f} segundos\n")

    print("10x10: ")
    inicio = time.time()
    solucao_warnsdorff10 = passeio_do_cavalo_warnsdorff(10)
    fim = time.time()
    imprimir_tabuleiro(solucao_warnsdorff10)
    print(f"Tempo para 10x10: {fim - inicio:.20f} segundos\n")

    print("\n=== Passeio do Cavalo (Força Bruta) ===")
    print("5x5: ")
    inicio = time.time()
    solucao_bruta5 = passeio_do_cavalo_forca_bruta(5)
    fim = time.time()
    imprimir_tabuleiro(solucao_bruta5)
    print(f"Tempo para 5x5 força bruta: {fim - inicio:.20f} segundos\n")

    print("6x6: ")
    inicio = time.time()
    solucao_bruta6 = passeio_do_cavalo_forca_bruta(6)
    fim = time.time()
    imprimir_tabuleiro(solucao_bruta6)
    print(f"Tempo para 6x6 força bruta: {fim - inicio:.20f} segundos\n")

    print("8x8: ")
    inicio = time.time()
    solucao_bruta8 = passeio_do_cavalo_forca_bruta(8)
    fim = time.time()
    imprimir_tabuleiro(solucao_bruta8)
    print(f"Tempo para 8x8 força bruta: {fim - inicio:.20f} segundos\n")

    print("10x10: ")
    inicio = time.time()
    solucao_bruta10 = passeio_do_cavalo_forca_bruta(10)
    fim = time.time()
    imprimir_tabuleiro(solucao_bruta10)
    print(f"Tempo para 10x10 força bruta: {fim - inicio:.20f} segundos\n")
