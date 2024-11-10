def encontrar_duplicados_forca_bruta(lista):
    duplicados = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j] and lista[i] not in duplicados:
                duplicados.append(lista[i])
    return duplicados

def encontrar_duplicados_set(lista):
    vistos = set()
    duplicados = []
    for num in lista:
        if num in vistos:
            duplicados.append(num)
        else:
            vistos.add(num)
    return duplicados


lista = [1, 2, 3, 2, 4, 1, 5]
print("Duplicados (Força Bruta):", encontrar_duplicados_forca_bruta(lista))
print("Duplicados (Set):", encontrar_duplicados_set(lista))