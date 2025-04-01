from alg2.tp1.MaxHeapComplet import MaxHeap
from alg2.tp1.Trie import Trie
from alg2.tp1.prioridadeMinHeap import MinHeap


def tp13():
    max_heap = MaxHeap([50, 30, 40, 10, 20, 35])
    max_heap.insert(45)
    print(max_heap)


def tp16():
    fila = MinHeap()

    while True:
        nome = input("Digite o nome (ou 'sair' para finalizar): ")
        if nome.lower() == 'sair':
            break
        try:
            prioridade = int(input(f"Digite a prioridade de {nome}: "))
            fila.inserir(nome, prioridade)
        except ValueError:
            print("Por favor, insira um número válido para a prioridade.")

    ordenados = fila.ordenar()

    print("\nFila de Prioridade Ordenada:")
    for item in ordenados:
        print(f"Nome: {item[0]}, Prioridade: {item[1]}")


def tp18():
    trie = Trie()
    trie.insert("casa")
    trie.insert("carro")
    trie.insert("caminhão")
    trie.insert("cachorro")
    trie.insert("cadeira")

    trie.show_hierarchy()


def tp110():
    trie = Trie()
    trie.insert("casa")
    trie.insert("carro")
    trie.insert("caminhão")
    trie.insert("cachorro")
    trie.insert("cadeira")

    print(f"Busca para o prefixo cad: {trie.busca_by_prefixo("cad")}")
    print(f"Busca para o prefixo ca: {trie.busca_by_prefixo("ca")}")

def tp112():
    trie = Trie()
    trie.insert("casa")
    trie.insert("carro")
    trie.insert("caminhão")
    trie.insert("cachorro")
    trie.insert("cadeira")

    print(f"Opções para o autocomplete do prefixo ca: {trie.busca_by_prefixo("ca")}")

if __name__ == "__main__":
    print("=========1.3===========")
    tp13()
    print("=========1.6===========")
    tp16()
    print("=========1.8===========")
    tp18()
    print("=========1.10===========")
    tp110()
    print("=========1.12===========")
    tp112()
