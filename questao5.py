def tarefa_no_topo(pilha_de_tarefas):
    if len(pilha_de_tarefas) == 0:
        return None
    return pilha_de_tarefas[-1]



pilha_de_tarefas = ["Tarefa 1", "Tarefa 2", "Tarefa 3", "Tarefa 4"]

tarefa = tarefa_no_topo(pilha_de_tarefas)
print("Tarefa no topo:", tarefa)  

pilha_de_tarefas.pop()

tarefa = tarefa_no_topo(pilha_de_tarefas)
print("Tarefa no topo após remoção:", tarefa)  

pilha_de_tarefas.pop()
pilha_de_tarefas.pop()
pilha_de_tarefas.pop()

tarefa = tarefa_no_topo(pilha_de_tarefas)
print("Tarefa no topo após esvaziar a pilha:", tarefa)  
