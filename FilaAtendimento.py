class FilaAtendimento:
    def __init__(self):
        self.itens = []

    def is_empty(self):
        return len(self.itens) == 0

    def adicionar_cliente(self, item):
        print(f"{item} entrou na fila")
        self.itens.append(item)

    def atender_cliente(self):
        if self.is_empty():
            print("A fila está vazia")
            return None

        cliente_atendido = self.itens.pop(0)
        print(f"{cliente_atendido} foi atendido")
        return cliente_atendido

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
