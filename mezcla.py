import random


def ordenamiento_por_mezcla(lista):
    mid = len(lista)//2
    if len(lista) > 1:
        L = lista[mid:]
        R = lista[:mid]

        lista.clear()

        ordenamiento_por_mezcla(L)
        ordenamiento_por_mezcla(R)

        while len(L) > 0 and len(R) > 0:
            if L[0] < R[0]:
                lista.append(L.pop(0))
            else:
                lista.append(R.pop(0))

        while len(L) > 0:
            lista.append(L.pop(0))
        while len(R) > 0:
            lista.append(R.pop(0))
        return lista


if __name__ == '__main__':
       tamano_de_lista = int(input('Deque tamaño sera la lista? '))

       lista = [random.randint(0, 100) for i in range(tamano_de_lista)]

       print(lista)
       print('-' * 20)
       lista_ordenada = ordenamiento_por_mezcla(lista)
       print(lista_ordenada)