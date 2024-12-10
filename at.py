import os
import time

from TabelaHash import TabelaHash


class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone


def buscar_telefone_contato(contatos, nome):
    for contato in contatos:
        if contato.nome.lower() == nome.lower():
            return contato.telefone
    return None


def busca_linear(list, elemento):
    iteracoes = 0
    for num in list:
        iteracoes += 1
        if num == elemento:
            return num, iteracoes
    return None


def busca_binaria(list, elemento):
    esq = 0
    dir = len(list) - 1
    iteracoes = 0

    while esq <= dir:
        iteracoes += 1
        meio = (esq + dir) // 2
        if list[meio] == elemento:
            return meio, iteracoes
        elif list[meio] < elemento:
            esq = meio + 1
        else:
            dir = meio - 1


def bubble_sort(arr):
    tempInicial = time.time()
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    temp_final = time.time() - tempInicial
    return arr, temp_final


def tem_duplicata(lista):
    tabela = TabelaHash()
    for li in lista:
        if tabela.buscar(li) is not None:
            return True
        else:
            tabela.inserir(li, li)
    return False


class Jogador:
    def __init__(self, nome, pontuacao):
        self.nome = nome
        self.pontuacao = pontuacao

    def __str__(self):
        return f"{self.nome} - {self.pontuacao} pontos"

    __repr__ = __str__


def selection_sort_jogadores(jogadores):
    n = len(jogadores)
    for i in range(n):
        max = i
        for j in range(i + 1, n):
            if jogadores[j].pontuacao > jogadores[max].pontuacao:
                max = j
        if max != i:
            jogadores[i], jogadores[max] = jogadores[max], jogadores[i]

    return jogadores


def getArquivos(caminho, nivel=0):
    with os.scandir(caminho) as itens:
        for item in itens:
            espaco = " " * (nivel * 4)
            if item.is_dir():
                getArquivos(item.path, nivel + 1)
            else:
                print(f"{espaco} Arquivo: {item.path}")


class ItemMochila:
    def __init__(self, nome, peso, valor):
        self.nome = nome
        self.peso = peso
        self.valor = valor

    def __str__(self):
        return f"{self.nome} - {self.peso} kg - valor {self.valor}"

    __repr__ = __str__


def knapsack(itens, w):
    n = len(itens)
    memo = [[0] * (w + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, w + 1):
            if itens[i - 1].peso > w:
                memo[i][w] = memo[i - 1][w]
            else:
                incluir = itens[i - 1].valor + memo[i - 1][w - itens[i - 1].peso]
                excluir = memo[i - 1][w]
                memo[i][w] = max(incluir, excluir)
    return memo[n][w]
