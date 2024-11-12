class FilaAtendimento:
    def __init__(self):
        self.itens = []

    def is_empty(self):
        return len(self.itens) == 0

    def adicionar_cliente(self, item):
        self.itens.append(item)

    def atender_cliente(self):
        if self.is_empty():
            print("A fila está vazia")
            return None
        return self.itens.pop(0)

    def peek(self):
        if self.is_empty():
            print("A fila está vazia")
            return None
        return self.itens[0]

    def tamanho_fila(self):
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
        return FilaAtendimento(list(self.itens))
