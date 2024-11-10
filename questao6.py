def contar_pedidos_impares(pilha_de_pedidos):
    contador = 0
    for pedido in pilha_de_pedidos:
        if pedido % 2 != 0:
            contador += 1
    return contador

pilha_pedidos = [1, 2, 3, 4, 5, 6, 7]
print("Número de pedidos ímpares:", contar_pedidos_impares(pilha_pedidos))
