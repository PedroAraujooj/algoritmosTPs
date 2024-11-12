import random

from Fila import Fila
from FilaAtendimento import FilaAtendimento
from Pilha import Pilha
from TabelaHash import TabelaHash

from tp1 import ex1, ex2, greatestNumber, ex6, ex8, ex9, ex10
from tp2 import merge_sort, tp2_ex3_a, tp2_ex3_b, ordernar_pilha, ordena_fila, tarefa_no_topo, tp2_ex6, tp2_ex7, \
    inverter_fila, tp2_ex10

if __name__ == '__main__':
    listaNum = list(range(1, 15))
    random.shuffle(listaNum)
    print("----------tp2-ex2---------------")
    print(merge_sort(listaNum))
    print("------------tp2-ex3-a-------------")
    print(tp2_ex3_a([0,1,1,9,75,7,76,7,766,72,7,9,3,9,7]))
    print("-------------tp2-ex3-b------------")
    print(tp2_ex3_b([0,1,1,9,75,7,76,7,766,72,7,9,3,9,7]))
    print("------------tp2-ex4-ordenar pilha-------------")
    pilha = Pilha([34, 3, 31, 98, 92, 23])
    pilha = ordernar_pilha(pilha, Pilha([]), None)
    pilha.display()
    print("------------tp2-ex5-------------")
    pilhaEx5 = Pilha([34, 3, 31, 98, 92, 23])
    tarefa_no_topo(pilhaEx5)
    print("------------tp2_ex6-------------")
    print(tp2_ex6(Pilha([34, 3, 31, 98, 92, 23])))
    print("------------tp2_ex7-------------")
    print(tp2_ex7(Pilha([34, 3, 31, 98, 92, 23])))
    print("------------tp2-ex8 - inverter_fila-------------")
    novaFilaInversa =  inverter_fila(Fila([34, 3, 31, 98, 92, 23]))
    novaFilaInversa.display()
    print("------------tp2-ex9 - ordena_fila-------------")
    fila = Fila([34, 3, 31, 98, 92, 23])
    fila = ordena_fila(fila)
    fila.display()
    print("------------tp2-ex10-------------")
    print(tp2_ex10(Fila([34, 3, 31, 98, 92, 23])))
    print("------------tp2-ex11-------------")

    filaAtendimento = FilaAtendimento()
    filaAtendimento.adicionar_cliente("Pedro")
    filaAtendimento.adicionar_cliente("João")
    filaAtendimento.atender_cliente()
    print(filaAtendimento.tamanho_fila())

    print("------------tp2-ex12-------------")

    tabela = TabelaHash(6)
    tabela.inserir(1, "Pedro")
    print(tabela.buscar(1))
    tabela.remover(1)
    print(tabela.buscar(1))




