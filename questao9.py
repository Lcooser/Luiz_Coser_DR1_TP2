def ordenar_lista(lista):
    n = len(lista)
    for i in range(n):
        trocou = False
        for j in range(n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocou = True
        if not trocou:
            break
    return lista

lista = [7, 3, 5, 2, 8, 6, 1]
print("Lista original:", lista)
lista_ordenada = ordenar_lista(lista)
print("Lista ordenada:", lista_ordenada)
