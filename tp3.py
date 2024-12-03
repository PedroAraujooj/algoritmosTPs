import os


def getDiretoriosAndArquivos(caminho, nivel=0):
    with os.scandir(caminho) as itens:
        for item in itens:
            espaco = " " * (nivel * 4)
            if item.is_dir():
                print(f"{espaco} Diretório: {item.path}")
                getDiretoriosAndArquivos(item.path, nivel + 1)
            else:
                print(f"{espaco} Arquivo: {item.path}")


def tores_de_hanoi(n, origem, destino, aux):
    if n == 1:
        print(f"Mova o disco 1 de {origem} para {destino}")
    else:
        tores_de_hanoi(n - 1, origem, aux, destino)
        print(f"Mova o disco {n} de {origem} para {destino}")
        tores_de_hanoi(n - 1, aux, destino, origem)


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def fatorial(n):
    if n <= 1:
        return n
    return n * fatorial(n - 1)


def quicksort(array):
    if len(array) <= 1:
        return array
    pivot = array[-1]
    menores = [x for x in array[:-1] if x <= pivot]
    maiores = [x for x in array[:-1] if x > pivot]
    return quicksort(menores) + [pivot] + quicksort(maiores)


def quickselect(array, low, high, k):
    if low == high:
        return array[low]
    pivot_index = partition(array, low, high)
    if k == pivot_index:
        return array[k]
    elif k < pivot_index:
        return quickselect(array, low, pivot_index - 1, k)
    else:
        return quickselect(array, pivot_index + 1, high, k)


def partition(array, low, high):
    pivot = array[high]
    i = low
    for j in range(low, high):
        if array[j] <= pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[i], array[high] = array[high], array[i]
    return i


def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


def fatorial_for(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


def percorrer_arvore(raiz):
    if raiz is None:
        return []
    return percorrer_arvore(raiz.esquerda) + [raiz.valor] + percorrer_arvore(raiz.direita)


def soma_lista_ex12(lista, total=0):
    if not lista:
        return total
    return soma_lista_ex12(lista[1:], total + lista[0])


def palindromo(palavra):
    if len(palavra) == 0:
        return True
    if palavra[0] == palavra[-1]:
        return palindromo(palavra[1:-1])
    else:
        return False


def soma_lista(lista):
    if not lista:
        return 0
    return soma_lista(lista[1:]) + lista[0]


def contar_repeticoes(palavra, letra):
    if len(palavra) == 0:
        return 0
    if palavra[0] == letra:
        return 1 + contar_repeticoes(palavra[1:], letra)
    else:
        return contar_repeticoes(palavra[1:], letra)


def inverter_string(palavra):
    if len(palavra) == 0:
        return ""
    return palavra[-1] + inverter_string(palavra[:-1])
