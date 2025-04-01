class Pacote:
    def __init__(self, id, tempoTrans, prioridade):
        self.id = id
        self.tempoTrans = tempoTrans
        self.prioridade = prioridade

    def __str__(self):
        return f'(ID: {self.id}  Prioridade: {self.prioridade})'

    def __repr__(self):
        return self.__str__()


class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, item):
        self.heap.append(item)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        while index > 0 and self.heap[index].prioridade < self.heap[parent_index].prioridade:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index - 1) // 2

    def _heapify_down(self, index):
        smallest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        if left_child < len(self.heap) and self.heap[left_child].prioridade < self.heap[smallest].prioridade:
            smallest = left_child
        if right_child < len(self.heap) and self.heap[right_child].prioridade < self.heap[smallest].prioridade:
            smallest = right_child

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def criar_heap_by_lista(self, lista):
        self.heap = lista[:]
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
            self._heapify_down(i)

    def exibir_heap(self):
        print(self.heap)

    def buscar(self, id):
        return self._buscar(0, id)

    def _buscar(self, index, id):
        if index >= len(self.heap):
            return False

        if self.heap[index].id == id:
            return True

        return (self._buscar(2 * index + 1, id) or
                self._buscar(2 * index + 2, id))

    def modificar_prioridade(self, id, nova_prioridade):
        for index, processo in enumerate(self.heap):
            if processo.id == id:
                old_priority = processo.prioridade
                processo.prioridade = nova_prioridade
                if nova_prioridade < old_priority:
                    self._heapify_up(index)
                elif nova_prioridade > old_priority:
                    self._heapify_down(index)
                return True
        return False


if __name__ == '__main__':
    proc1 = Pacote(1, 40, 4)
    proc2 = Pacote(2, 100, 10)
    proc3 = Pacote(3, 30, 3)
    proc4 = Pacote(4, 50, 5)
    proc5 = Pacote(5, 10, 1)

    lista_inteiros = [proc1, proc2, proc3, proc4, proc5]

    min_heap = MinHeap()
    min_heap.criar_heap_by_lista(lista_inteiros)
    print("Heap antes da modificação:")
    min_heap.exibir_heap()

    min_heap.insert(Pacote(6, 60, 6))
    print("\nHeap após adição do pacote de rede de ID 6:")
    min_heap.exibir_heap()

    min_heap.pop()
    print("\nHeap após execução do próximo pacote de maior prioridade:")
    min_heap.exibir_heap()

    min_heap.modificar_prioridade(2, 2)
    print("\nHeap após modificação da prioridade do pacote com id 2 para 2:")
    min_heap.exibir_heap()