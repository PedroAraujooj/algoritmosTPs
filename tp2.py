from Fila import Fila
from Pilha import Pilha


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    meio = len(arr) // 2
    esquerda = arr[:meio]
    direita = arr[meio:]

    esquerda = merge_sort(esquerda)
    direita = merge_sort(direita)
    return merge(esquerda, direita)


def merge(esquerda, direita):
    return_arr = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            return_arr.append(esquerda[i])
            i += 1
        else:
            return_arr.append(direita[j])
            j += 1

    return_arr.extend(esquerda[i:])
    return_arr.extend(direita[j:])

    return return_arr


def tp2_ex3_a(arr):
    resul = set()
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                resul.add(arr[i])
        for j in range(0, i):
            if arr[i] == arr[j]:
                resul.add(arr[i])
    return resul


def tp2_ex3_b(arr):
    resul = set()
    visto = set()
    for i in range(len(arr)):
        if arr[i] in visto:
            resul.add(arr[i])
        else:
            visto.add(arr[i])
    return resul


def ordernar_pilha(pilha, temp, ele):
    if pilha.peek() == "A pilha está vazia":
        temp.push(ele)
        return temp
    if not ele:
        ele = pilha.pop()
    if ele < float(pilha.peek()):
        temp.push(ele)
        ele = pilha.pop()
        return ordernar_pilha(pilha, temp, ele)
    else:
        temp.push(ele)
        ele = pilha.pop()
        while temp.peek() != "A pilha está vazia" and temp.peek() > ele:
            pilha.push(temp.pop())
        temp.push(ele)
        ele = pilha.pop()
        return ordernar_pilha(pilha, temp, ele)

def tarefa_no_topo(pilha):
    print("A tarefa mais recente é a : " + str(pilha.peek()))

def tp2_ex6(pilha):
    qntd = 0
    temp = pilha.clonar()

    while temp.peek() != "A pilha está vazia":
        if temp.pop() % 2 == 1:
            qntd += 1
    return qntd

def tp2_ex7(pilha):
    qntd = 0
    temp = pilha.clonar()

    while temp.peek() != "A pilha está vazia":
        if temp.pop() % 2 == 0:
            qntd += 1
    return qntd

def inverter_fila(fila):
    if fila.is_empty():
        return
    item = fila.dequeue()
    inverter_fila(fila)
    fila.enqueue(item)
    return fila


def ordena_fila(fila):
    if fila.is_empty():
        return fila
    fila_retorno = Fila([])
    while not fila.is_empty():
        mim = fila.dequeue()
        fila_temp = Fila([])
        while not fila.is_empty():
            ele = fila.dequeue()
            if ele < mim:
                fila_temp.enqueue(mim)
                mim = ele
            else:
                fila_temp.enqueue(ele)
        fila_retorno.enqueue(mim)
        while not fila_temp.is_empty():
            fila.enqueue(fila_temp.dequeue())
    return fila_retorno

def tp2_ex10(fila):
    qntd = 0
    temp = fila.clonar()

    while temp.peek() is not None:
        if temp.dequeue() % 2 == 1:
            qntd += 1
    return qntd