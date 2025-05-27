class Utilities:

    @staticmethod
    def validate_task_name(name):
        return len(name.strip()) > 0

    @staticmethod
    def mostrar_menu():
        print("\n" + "=" * 50)
        print("📋 TO-DO LIST".center(50))
        print("=" * 50)
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Remover Tarefa")
        print("4. Editar Tarefa")
        print("5. Sair")

    @staticmethod
    def validate_priority(string):
        if string in ["alta", "média", "baixa"]:
            return True
        return False
