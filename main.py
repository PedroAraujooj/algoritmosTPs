import random

from ArvoreBinaria import BinaryTree
from Fila import Fila
from FilaAtendimento import FilaAtendimento
from Pilha import Pilha
from TabelaHash import TabelaHash
from at import Contato, buscar_telefone_contato, busca_binaria, busca_linear, bubble_sort, tem_duplicata, \
    selection_sort_jogadores, Jogador, getArquivos, ItemMochila, knapsack

from tp1 import ex1, ex2, greatestNumber, ex6, ex8, ex9, ex10
from tp2 import merge_sort, tp2_ex3_a, tp2_ex3_b, ordernar_pilha, ordena_fila, tarefa_no_topo, tp2_ex6, tp2_ex7, \
    inverter_fila, tp2_ex10
from tp3 import getDiretoriosAndArquivos, tores_de_hanoi, fibonacci, fatorial, contar_repeticoes, inverter_string, \
    percorrer_arvore, soma_lista_ex12, palindromo, soma_lista

if __name__ == '__main__':
    print("=========== questão 3 ==============")
    lista_contatos = [Contato("Pedro", "123456789"), Contato("Agatha", "987654321"), Contato("Gilherme", "741852963"),
                      Contato("Alexandre", "987456852")]
    print(buscar_telefone_contato(lista_contatos, "pedro"))
    print(buscar_telefone_contato(lista_contatos, "agatha"))

    print("=========== questão 4 ==============")
    listaNum = list(range(0, 100000))
    print(busca_binaria(listaNum, 50000))
    print(busca_linear(listaNum, 50000))

    print("=========== questão 6 ==============")
    listaMil = list(range(0, 1000))
    lista10Mil = list(range(0, 10000))
    random.shuffle(listaMil)
    random.shuffle(lista10Mil)
    print(bubble_sort(listaMil)[1])
    print(bubble_sort(lista10Mil)[1])

    print("=========== questão 7 ==============")
    print(tem_duplicata([1, 2, 3, 4, 5, 3]))
    print(tem_duplicata([1, 2, 3, 4, 5]))

    print("=========== questão 8 ==============")
    print(selection_sort_jogadores([
        Jogador("Alice", 50),
        Jogador("Carlos", 10),
        Jogador("Bruno", 30),
        Jogador("Diana", 20)
    ]))

    print("=========== questão 9 ==============")


    class Perfil:
        def __init__(self, nome, idade):
            self.nome = nome
            self.idade = idade

        def __str__(self):
            return f"{self.nome} - {self.idade} anos de idade"

        __repr__ = __str__


    perfis = TabelaHash()
    perfis.inserir("alice", Perfil("Alice", 25))
    perfis.inserir("bruno", Perfil("Bruno", 30))
    perfis.inserir("carla", Perfil("Carla", 22))

    print(perfis.buscar("bruno"))
    print(perfis.buscar("daniel"))

    print("=========== questão 10 ==============")


    class Navegador:
        def __init__(self, pagina_inicial):
            self.stack_voltar = Pilha()
            self.stack_avancar = Pilha()
            self.pagina_atual = pagina_inicial

        def visitar_pagina(self, nova_pagina):
            self.stack_voltar.push(self.pagina_atual)
            self.stack_avancar = Pilha()
            self.pagina_atual = nova_pagina
            print(f"Visitando: {self.pagina_atual}")

        def voltar(self):
            if self.stack_voltar.is_empty():
                print("Erro. Não a página para voltar")
                return
            self.stack_avancar.push(self.pagina_atual)
            self.pagina_atual = self.stack_voltar.pop()
            print(f"Voltando para: {self.pagina_atual}")

        def avancar(self):
            if self.stack_avancar.is_empty():
                print("Erro. Não a página para avançar")
                return
            self.stack_voltar.push(self.pagina_atual)
            self.pagina_atual = self.stack_avancar.pop()
            print(f"Avançando para: {self.pagina_atual}")

        def pagina_corrente(self):
            return self.pagina_atual


    navegador = Navegador("home.com")
    navegador.visitar_pagina("google.com")
    navegador.visitar_pagina("wikipedia.com")
    navegador.visitar_pagina("github.com")
    navegador.voltar()
    navegador.voltar()
    navegador.avancar()

    print("=========== questão 11 ==============")

    filaAtendimento = FilaAtendimento()
    filaAtendimento.adicionar_cliente("Pedro")
    filaAtendimento.adicionar_cliente("João")
    filaAtendimento.atender_cliente()
    print(f"tamanho atual da fila: {filaAtendimento.tamanho_fila()}")

    print("=========== questão 12 ==============")
    getArquivos("dir1")

    print("=========== questão 13 ==============")
    itens = [
        ItemMochila("Item1", peso=2, valor=3),
        ItemMochila("Item2", peso=3, valor=4),
        ItemMochila("Item3", peso=4, valor=5),
        ItemMochila("Item4", peso=5, valor=6)
    ]
    valor_maximo = knapsack(itens, 5)
    print("Valor máximo que pode ser carregado:", valor_maximo)

    print("=========== questão 14 ==============")
    bst = BinaryTree()

    bst.add(100)
    bst.add(50)
    bst.add(150)
    bst.add(30)
    bst.add(70)
    bst.add(130)
    bst.add(170)

    print("Árvore binária de buscaem ordem:", bst.inorder())

    valor_busca = 70
    encontrado = bst.search(valor_busca)
    if encontrado:
        print(f"Preço {valor_busca} encontrado na árvore binária de busca.")
    else:
        print(f"Preço {valor_busca} não encontrado na árvore binária de busca.")

    print("=========== questão 15 ==============")

    notas = [85, 70, 95, 60, 75, 90, 100]
    arvore15 = BinaryTree()
    arvore15.add(85)
    arvore15.add(70)
    arvore15.add(95)
    arvore15.add(60)
    arvore15.add(75)
    arvore15.add(90)
    arvore15.add(100)
    print("Árvore em ordem:", arvore15.inorder())
    minimo = arvore15.get_min_value()
    print("Nota mínima:", minimo)
    maximo = arvore15.get_max_value()
    print("Nota máxima:", maximo)

    print("=========== questão 16 ==============")
    arvore16 = BinaryTree()
    arvore16.add(45)
    arvore16.add(25)
    arvore16.add(65)
    arvore16.add(20)
    arvore16.add(30)
    arvore16.add(60)
    arvore16.add(70)

    print("Árvore inicial:", arvore16.inorder())
    arvore16.remove(20)
    print("Após remover o nó 20:", arvore16.inorder())
    arvore16.remove(25)
    print("Após remover o nó 25:", arvore16.inorder())
    arvore16.remove(45)
    print("Após remover o nó 45:", arvore16.inorder())