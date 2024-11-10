def ordenar_pilha(pilha):
    if len(pilha) <= 1:
        return pilha
    topo = pilha.pop()
    ordenar_pilha(pilha)
    inserir_ordenado(pilha, topo)
    return pilha

def inserir_ordenado(pilha, elemento):
    if not pilha or pilha[-1] <= elemento:
        pilha.append(elemento)
    else:
        topo = pilha.pop()
        inserir_ordenado(pilha, elemento)
        pilha.append(topo)

pilha = [5, 1, 3, 7, 2]
print("Pilha original:", pilha)
pilha_ordenada = ordenar_pilha(pilha)
print("Pilha ordenada:", pilha_ordenada)
