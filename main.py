import random


def ex1():
    caracteres = [x for x in "Sítio do pica-pau amarelo \n 2023" if not x.isspace()]
    for x in caracteres:
        print(x)


def ex2():
    mao1 = [13, 8, 12, 2, 6, 9, 1, 11, 3, 4, 5, 10, 7]
    for i in range(0, len(mao1)):
        for j in range(i, len(mao1)):
            if mao1[j] < mao1[i]:
                mao1[j], mao1[i] = mao1[i], mao1[j]
    print(mao1)


def greatestNumber(array):
    if len(array) == 0:
        print("Array vazio")
        return
    greatest = array[0]
    for i in array:
        if i > greatest:
            greatest = i
    return greatest

def ex6(num):
    return (pow(num, 1/2)) + 1

def ex8(arr):
    for i in range(len(arr) - 1, int((len(arr)/2) - 1), -1):
        k = int((len(arr)/2))
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

        for j in range(i, k, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    print(arr)

def ex9(arr):
    print("velha lista: ")
    print(arr)
    for i in range(len(arr)-1, 0 , -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print("nova lista: ")
    print(arr)

def ex10(arr):
    print("velha lista: ")
    print(arr)
    for i in range(len(arr)-1, 0 , -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print("nova lista: ")
    print(arr)

if __name__ == '__main__':
    listaNum = list(range(1, 14))
    random.shuffle(listaNum)

    listaString = ["Maçã", "Banana", "Laranja", "Uva", "Morango", "Abacaxi", "Melancia", "Pêssego", "Ameixa", "Kiwi", "Manga", "Cereja", "Limão"]

    ex10(listaString)
