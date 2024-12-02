import os


def getDiretoriosAndArquivos(caminho, nivel=0):
    # O bigO será de O(N) sendo N a quantidade de arquivos + subdiretorios, pois a funão percorerá todos eles uma vez, pois percorerá
    #primeiro cada arquivo do caminho e depois cada arquivo presente em seus subdiretorios apartir de recursividade
    with os.scandir(caminho) as itens:
        for item in itens:
            espaco = " " * (nivel * 4)
            if item.is_dir():
                print(f"{espaco} Diretório: {item.path}")
                getDiretoriosAndArquivos(item.path, nivel + 1)
            else:
                print(f"{espaco} Arquivo: {item.path}")

def tores_de_hanoi(n, origem, destino, aux):
    #O algarismo trabalha seguindo o principio que o dico maior é movido apenas quando os discos menores forem removidos do "caminho"
    #primeiramente, ele Move n-1 discos da origem para o pino auxiliar
    #após isso, move os discos restantes para da origem para o destino
    #por fim, move os n-1 discos do pino auxiliar para o de destino
    #até chegar no caso de base n == 1
    if n == 1:
        print(f"Mova o disco 1 de {origem} para {destino}")
    else:
        tores_de_hanoi(n - 1, origem, aux, destino)
        print(f"Mova o disco {n} de {origem} para {destino}")
        tores_de_hanoi(n - 1, aux, destino, origem)

def fibonacci(n):
    #Possui o Big O de O(N²) pois a cada chamada N, ele executa recursivamnete as chamadas de de N-1 e N-2, se tornando um número de chmadas exponensial
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def fatorial(n):
    #Possui o Big O de O(N) pois a cada chamada N, ele executa recursivamnete a chamada de de N-1 apenas, sendo uma algoritmo linear
    if n <= 1:
        return n
    return n * fatorial(n - 1)

def quicksort(array):
    #O algoritmo funciona por meio da recursão da seguinte forma: primeiro é escolhido um pivot(no  caso desse algoritmo, é o ultimo elemento do array)
    #e a partir dde pivot, ele divide o array em outros 2 arrays, o com os valores menores que o pivot e um outro com os valores menores
    #entre ele contatena o array resultande da chamada recursica do arrey de valores menores com o pivot e com o array resultande da chamada recursica do array de valores maiores
    #até o valor base, que é o array de tamanho 1 ou 0, que retorna o proprio array

    #O BigO será de O(N²) pois no pior caso, sendo o pivot o maior numero ou menor numero, ele executara a recursão de um array de ,tamanho n-1, n vezes
    #
    #

    if len(array) <= 1:
        return array
    pivot = array[-1]
    menores = [x for x in array[:-1] if x <= pivot]
    maiores = [x for x in array[:-1] if x > pivot]
    return quicksort(menores) + [pivot] + quicksort(maiores)

def quickselect(array, low, high, k):
    #A funão tem como base quanto o arrey tem apenas 1 elemento, retornando esse unico eelemento
    #primeramente, a fução chama a função partition(array, low, high) que move o pivot para posicao correta e organiza os outros elementos do array
    #na posição correta, os menores a esquerda do pivot e maiores a direta
    # após isso, verifica a posiçao do pivot, se for igual a K, ele retorna o elemento na posição k(array[k])
    #senão, caso o k seja menor que o pivot, ele chama a função recursivamente, substituindo o "high", pelo pivot_index - 1
    # e caso k sehja maior, chama recrsivamente substituindo o "low" por pivot index + 1

    #como nesse caso o BigO no pior caso será O(N²), e o BigO da busca linear no pior caso será O(N), a busca linear se torna mais eficiente
    if low == high:
        return array[low]
    pivot_index = partition(array, low, high)
    if k == pivot_index:
        return array[k]
    elif k < pivot_index:
        return quickselect(array, low, pivot_index - 1, k)
    else:
        return quickselect(array, pivot_index + 1, high, k)

def partition(array, low, high):
    pivot = array[high]
    i = low
    for j in range(low, high):
        if array[j] <= pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[i], array[high] = array[high], array[i]
    return i

#o problema de trablahr com funções recursivas pode ser a quantidade de chamadas feitas, causando o famoso "stackoverflow"
#mas há formas de contornar esses casos, como por exemplo, usar  iteração ou armazenar(memorizar) os valores já colculados
#demostração em fibonacci_memo, onde armazendo os valores jácalculados, e fatorial_for, onde subistituo a recursividade por uma iteração no "for"

def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

def fatorial_for(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def percorrer_arvore(raiz):
    #a recursão facilita a navegação por estruturas hierárquicas pois elas são naturalmente recursivas, pois cada nó de uma arvore pode ser considerado o
    #nó raiz de uma subarvore, ou seja, a logica da aplicação pode ser ultilizada da mesma forma em um nó e nos seus filhos
    #além disso se torna uma forma eficiente por acessar cada nó apenas uma vez
    if raiz is None:
        return []
    return percorrer_arvore(raiz.esquerda) + [raiz.valor] + percorrer_arvore(raiz.direita)

#o ponto o Stack Overflow na funçao fatorial ocorrre quando passado o valor 1000, pois ele executará mil chamadas, que é o limite de chamadas default do python.
#usa solução seria usar a iteração ao inves da recursividade, um exemplo está implemtando na função fatorial_for

def soma_lista_ex12(lista, total=0):
    if not lista:
        return total
    return soma_lista_ex12(lista[1:], total + lista[0])

def palindromo(palavra):
    if len(palavra) == 0:
        return True
    if palavra[0] == palavra[-1]:
        return palindromo(palavra[1:-1])
    else:
        return False

def soma_lista(lista):
    if not lista:
        return 0
    return soma_lista(lista[1:]) + lista[0]

def contar_repeticoes(palavra, letra):
    if len(palavra) == 0:
        return 0
    if palavra[0] == letra:
        return 1 + contar_repeticoes(palavra[1:], letra)
    else:
        return contar_repeticoes(palavra[1:], letra)

def inverter_string(palavra):
    if len(palavra) == 0:
        return ""
    return palavra[-1] + inverter_string(palavra[:-1])