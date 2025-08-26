# arquivo task manager
from Modelos.utilities import Utilities
from task import Task


class TaskManager:

    def __init__(self):
        self.tarefas = []
        #teste13

    def adicionar_tarefa(self, titulo, descricao, prioridade="------"):
        nova_tarefa = Task(titulo, descricao, prioridade)
        self.tarefas.append(nova_tarefa)

    def listar_tarefas(self):
        for i, tarefa in enumerate(self.tarefas, 1):
            print(f"\n🔷 Tarefa {i}")
            print(tarefa)
        #reste arroz

    def editar_tarefa(self, tarefa_idx, campo, novo_valor):
        tarefa = self.tarefas[tarefa_idx]

        # Validação específica para prioridade
        if campo == "prioridade":
            if not Utilities.validate_priority(novo_valor):
                return False

        # Atualiza o campo se existir na tarefa
        if hasattr(tarefa, campo):
            setattr(tarefa, campo, novo_valor)
            return True
        return False

    def marcar_concluida(self, num_tarefa):
        self.tarefas[num_tarefa].status = "Concluida"

    def remover_tarefa(self, num_tarefa):
        num_tarefa -= 1
        self.tarefas.pop(num_tarefa)
