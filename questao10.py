from collections import deque

def contar_livros_impares(fila):
    contador = 0
    for livro in fila:
        if livro % 2 != 0:
            contador += 1
    return contador

fila_livros = deque([1, 2, 3, 4, 5, 6, 7])
print("Número de livros com identificação ímpar:", contar_livros_impares(fila_livros))
