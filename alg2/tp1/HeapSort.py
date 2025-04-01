class HeapSort:
    def __init__(self, lista):
        self.lista = lista
        self.n = len(lista)

    def _heapify(self, indice, tamanho):
        """Ajusta o heap para manter a propriedade do heap máximo"""
        maior = indice
        esq = 2 * indice + 1  # Filho esquerdo
        dir = 2 * indice + 2  # Filho direito

        if esq < tamanho and self.lista[esq] > self.lista[maior]:
            maior = esq
        if dir < tamanho and self.lista[dir] > self.lista[maior]:
            maior = dir

        if maior != indice:
            self.lista[indice], self.lista[maior] = self.lista[maior], self.lista[indice]
            self._heapify(maior, tamanho)

    def ordenar(self):
        """Realiza a ordenação com o algoritmo Heap Sort"""
        # Construa o heap (max heap)
        for i in range(self.n // 2 - 1, -1, -1):
            self._heapify(i, self.n)

        # Um por um, extraímos os elementos do heap e colocamos na posição correta
        for i in range(self.n - 1, 0, -1):
            # Move o maior item para o final
            self.lista[0], self.lista[i] = self.lista[i], self.lista[0]
            # Chama o heapify na parte reduzida do heap
            self._heapify(0, i)

        return self.lista


# Função para solicitar números do usuário
def solicitar_dados():
    lista = []
    while True:
        entrada = input("Digite um número (ou digite 'sair' para finalizar): ")
        if entrada.lower() == 'sair':
            break
        try:
            num = int(entrada)
            lista.append(num)
        except ValueError:
            print("Por favor, insira um número válido ou 'sair' para finalizar.")

    if lista:  # Verifica se a lista não está vazia antes de ordenar
        print("\nLista original:", lista)

        heap_sort = HeapSort(lista)
        lista_ordenada = heap_sort.ordenar()

        print("Lista ordenada:", lista_ordenada)
    else:
        print("Nenhum número foi inserido.")

    # Pausa para não fechar imediatamente o terminal
    input("\nPressione Enter para sair...")


# Garantir que o código seja executado corretamente no terminal
if __name__ == "__main__":
    solicitar_dados()
