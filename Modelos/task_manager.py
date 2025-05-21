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

    def editar_tarefa(self, num_tarefa):
        print("\n" + "=" * 50)
        print("📋 MODO DE EDIÇÃO".center(50))
        print("=" * 50)
        print("1. Titulo")
        print("2. Descrição")
        print("3. Prioridade")
        print("4. Sair")


        escolha = int(input("👉 Escolha uma opção: "))

        match escolha:
            case 1:
                novo_titulo = input("Digite o novo titulo: ")
                self.tarefas[num_tarefa - 1].titulo = novo_titulo

            case 2:
                nova_descricao = input("Digite o novo titulo: ")
                self.tarefas[num_tarefa - 1].descricao = nova_descricao
            case 3:
                nova_prioridade = input("Digite o novo titulo: ")
                self.tarefas[num_tarefa - 1].prioridade = nova_prioridade
            case 4:
                return
            case _:
                return "Digite uma opção válida"

    def remover_tarefa(self, num_tarefa):
        num_tarefa -= 1
        self.tarefas.pop(num_tarefa)

manager = TaskManager()

#Adicionar tarefas
manager.adicionar_tarefa("Pau", "no seu cu")
manager.adicionar_tarefa("Nabu", "Nabu Nabu Nabu Nabucetinha")
manager.adicionar_tarefa("Nescau", "Toddy")

#Listando tarefas
manager.listar_tarefas()

#Editando tarefas

manager.editar_tarefa(2)

manager.listar_tarefas()