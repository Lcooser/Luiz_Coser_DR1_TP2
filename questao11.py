from collections import deque

class FilaAtendimento:
    def __init__(self):
        self.fila = deque()

    def adicionar_cliente(self, nome):
        self.fila.append(nome)
        print(f"Cliente {nome} adicionado.")

    def atender_cliente(self):
        if len(self.fila) > 0:
            cliente = self.fila.popleft()
            print(f"Atendendo {cliente}")
        else:
            print("Fila vazia!")

    def tamanho_fila(self):
        return len(self.fila)

fila = FilaAtendimento()

fila.adicionar_cliente("Flavio")
fila.adicionar_cliente("Luiz")
fila.adicionar_cliente("Carlos")

print("Clientes na fila:", fila.tamanho_fila())

fila.atender_cliente()
fila.atender_cliente()

print("Clientes na fila:", fila.tamanho_fila())

fila.atender_cliente()
fila.atender_cliente()
