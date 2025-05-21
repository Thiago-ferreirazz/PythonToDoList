from task_manager import TaskManager


def mostrar_menu():
    print("\n" + "=" * 50)
    print("📋 TO-DO LIST".center(50))
    print("=" * 50)
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Remover Tarefa")
    print("4. Sair")


def main():
    manager = TaskManager()

    while True:
        mostrar_menu()
        opcao = input("👉 Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Título: ")
            descricao = input("Descrição: ")
            while True:
                prioridade = input("Prioridade [baixa, média ou alta]: ") or "média"
                if prioridade  in ["baixa", "média", "alta"]:
                    break
                print("Digite um termo válido!")


            manager.adicionar_tarefa(titulo, descricao, prioridade)
            print("\n✅ Tarefa adicionada!")

        elif opcao == "2":
            print("\n" + "📋 LISTA DE TAREFAS" + "=" * 30)
            manager.listar_tarefas()

        elif opcao == "3":
            try:
                indice = int(input("Número da tarefa a remover: "))
                manager.remover_tarefa(indice)
                print("\n🗑️ Tarefa removida!")
            except (ValueError, IndexError) as e:
                print(f"\n❌ Erro: {e}")

        elif opcao == "4":
            print("\n👋 Até logo!")
            break

        else:
            print("\n❌ Opção inválida!")


if __name__ == "__main__":
    main()