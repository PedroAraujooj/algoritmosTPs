import random

from Fila import Fila
from FilaAtendimento import FilaAtendimento
from Pilha import Pilha
from TabelaHash import TabelaHash

from tp1 import ex1, ex2, greatestNumber, ex6, ex8, ex9, ex10
from tp2 import merge_sort, tp2_ex3_a, tp2_ex3_b, ordernar_pilha, ordena_fila, tarefa_no_topo, tp2_ex6, tp2_ex7, \
    inverter_fila, tp2_ex10
from tp3 import getDiretoriosAndArquivos, tores_de_hanoi, fibonacci, fatorial, contar_repeticoes, inverter_string, Node, \
    percorrer_arvore

if __name__ == '__main__':
    getDiretoriosAndArquivos("dir1")
    tores_de_hanoi(4, 'A', 'B', 'C')
    print(fibonacci(10))
    raiz = Node(4)
    raiz.esquerda = Node(2)
    raiz.direita = Node(6)
    raiz.esquerda.esquerda = Node(1)
    raiz.esquerda.direita = Node(3)
    raiz.direita.esquerda = Node(5)
    raiz.direita.direita = Node(7)

    print(percorrer_arvore(raiz))

    print(contar_repeticoes("banana", "a"))
    print(inverter_string("recursao"))




