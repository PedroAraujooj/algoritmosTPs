class Pilha:
    def __init__(self):
        self.itens = []

    def __init__(self, lista):
        self.itens = lista

    def is_empty(self):
        return len(self.itens) == 0

    def push(self, item):
        self.itens.append(item)

    def pop(self):
        if not self.is_empty():
            return self.itens.pop()
        else:
            return "A pilha está vazia"

    def peek(self):
        if not self.is_empty():
            return self.itens[-1]
        else:
            return "A pilha está vazia"

    def size(self):
        return len(self.itens)

    def display(self):
        print("Pilha:", self.itens)

    def clonar(self):
        return Pilha(list(self.itens))