from task import Task

class TaskManager:

    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, titulo, descricao, prioridade = "------"):
        nova_tarefa = Task(titulo, descricao, prioridade)
        self.tarefas.append(nova_tarefa)

    def listar_tarefas(self):
        for i, tarefa in enumerate(self.tarefas, 1):
            print(f"\n🔷 Tarefa {i}")
            print(tarefa)

    def remover_tarefa(self, num_tarefa):
        num_tarefa -= 1
        self.tarefas.pop(num_tarefa)