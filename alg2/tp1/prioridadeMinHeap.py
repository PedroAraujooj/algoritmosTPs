class MinHeap:
    def __init__(self):
        self.heap = []

    def _heapify(self, indice, tamanho):
        menor = indice
        esq = 2 * indice + 1
        dir = 2 * indice + 2
        if esq < tamanho and self.heap[esq][1] < self.heap[menor][1]:
            menor = esq
        if dir < tamanho and self.heap[dir][1] < self.heap[menor][1]:
            menor = dir
        if menor != indice:
            self.heap[indice], self.heap[menor] = self.heap[menor], self.heap[indice]
            self._heapify(menor, tamanho)

    def inserir(self, nome, prioridade):
        self.heap.append((nome, prioridade))
        indice = len(self.heap) - 1

        while indice > 0:
            pai = (indice - 1) // 2
            if self.heap[indice][1] < self.heap[pai][1]:
                self.heap[indice], self.heap[pai] = self.heap[pai], self.heap[indice]
                indice = pai
            else:
                break

    def remover(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        raiz = self.heap[0]
        self.heap[0] = self.heap.pop()

        self._heapify(0, len(self.heap))

        return raiz

    def esta_vazia(self):
        return len(self.heap) == 0

    def ordenar(self):
        resultado = []
        while not self.esta_vazia():
            resultado.append(self.remover())
        return resultado




