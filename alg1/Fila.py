class Fila:
    def __init__(self):
        self.itens = []

    def __init__(self, list):
        self.itens = list

    def is_empty(self):
        return len(self.itens) == 0

    def enqueue(self, item):
        self.itens.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.itens.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.itens[0]

    def size(self):
        return len(self.itens)

    def display(self):
        if self.is_empty():
            print("A fila está vazia")
        else:
            print("Fila:", end=" ")
            for item in self.itens:
                print(item, end=" ")
            print()

    def clonar(self):
        return Fila(list(self.itens))
