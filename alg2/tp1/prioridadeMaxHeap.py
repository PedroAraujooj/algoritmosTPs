class FilaPrioridadeHeap:
    def __init__(self):
        self.heap = []

    def _heapify(self, indice, tamanho):
        """Ajusta o heap para manter a propriedade do heap máximo"""
        maior = indice
        esq = 2 * indice + 1  # Filho esquerdo
        dir = 2 * indice + 2  # Filho direito

        if esq < tamanho and self.heap[esq][1] > self.heap[maior][1]:
            maior = esq
        if dir < tamanho and self.heap[dir][1] > self.heap[maior][1]:
            maior = dir

        if maior != indice:
            self.heap[indice], self.heap[maior] = self.heap[maior], self.heap[indice]
            self._heapify(maior, tamanho)

    def inserir(self, nome, prioridade):
        """Insere um novo elemento na fila de prioridade"""
        self.heap.append((nome, prioridade))
        indice = len(self.heap) - 1

        # Ajusta o heap para manter a propriedade do heap máximo
        while indice > 0:
            pai = (indice - 1) // 2
            if self.heap[indice][1] > self.heap[pai][1]:
                self.heap[indice], self.heap[pai] = self.heap[pai], self.heap[indice]
                indice = pai
            else:
                break

    def remover(self):
        """Remove o item de maior prioridade da fila"""
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        # O item de maior prioridade está na raiz (índice 0)
        raiz = self.heap[0]
        self.heap[0] = self.heap.pop()

        # Reajusta o heap após remover o item
        self._heapify(0, len(self.heap))

        return raiz

    def esta_vazia(self):
        """Verifica se a fila de prioridade está vazia"""
        return len(self.heap) == 0

    def ordenar(self):
        """Ordena todos os elementos da fila de prioridade"""
        resultado = []
        while not self.esta_vazia():
            resultado.append(self.remover())
        return resultado


# Função para solicitar os dados ao usuário
def solicitar_dados():
    fila = FilaPrioridadeHeap()
    
    while True:
        nome = input("Digite o nome (ou 'sair' para finalizar): ")
        if nome.lower() == 'sair':
            break
        try:
            prioridade = int(input(f"Digite a prioridade de {nome}: "))
            fila.inserir(nome, prioridade)
        except ValueError:
            print("Por favor, insira um número válido para a prioridade.")

    # Ordenando os itens pela prioridade
    ordenados = fila.ordenar()

    # Exibindo a fila de prioridade ordenada
    print("\nFila de Prioridade Ordenada (do maior para o menor):")
    for item in ordenados:
        print(f"Nome: {item[0]}, Prioridade: {item[1]}")

    # Pausa para não fechar imediatamente o terminal
    input("\nPressione Enter para sair...")


# Garantir que o código seja executado corretamente no terminal
if __name__ == "__main__":
    solicitar_dados()
