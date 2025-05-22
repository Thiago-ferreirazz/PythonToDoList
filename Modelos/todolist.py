from task_manager import TaskManager
from utilities import Utilities


def main():
    manager = TaskManager()

    while True:
        Utilities.mostrar_menu()
        opcao = input("👉 Escolha uma opção: ")

        match opcao:
            case "1":
                titulo = input("Título: ")
                descricao = input("Descrição: ")
                while True:
                    prioridade = input("Prioridade [baixa, média ou alta]: ") or "média"
                    if prioridade in ["baixa", "média", "alta"]:
                        break
                    print("❌ Digite um termo válido!")
                manager.adicionar_tarefa(titulo, descricao, prioridade)
                print("\n✅ Tarefa adicionada!")

            case "2":
                print("\n" + "📋 LISTA DE TAREFAS" + "=" * 30)
                manager.listar_tarefas()

            case "3":
                try:
                    indice = int(input("Número da tarefa a remover: ")) - 1
                    manager.remover_tarefa(indice)
                    print("\n🗑️ Tarefa removida!")
                except (ValueError, IndexError) as e:
                    print(f"\n❌ Erro: {e}")

            case "4":
                if not manager.tarefas:
                    print("\n❌ Nenhuma tarefa para editar!")
                    continue

                while True:
                    print("\n" + "=" * 50)
                    print("📋 MODO DE EDIÇÃO".center(50))
                    print("=" * 50)

                    try:
                        print("\nOpções:")
                        print("1. Editar título")
                        print("2. Editar descrição")
                        print("3. Editar prioridade")
                        print("4. Marcar como Concluida")
                        print("5. Cancelar")

                        escolha = input("👉 Escolha uma opção: ")

                        manager.listar_tarefas()

                        tarefa_idx = int(input("\nNúmero da tarefa: ")) - 1
                        if not (0 <= tarefa_idx < len(manager.tarefas)):
                            print("❌ Tarefa inválida!")
                            continue

                        match escolha:
                            case "1":
                                novo_valor = input("Novo título: ")
                                manager.editar_tarefa(tarefa_idx, "titulo", novo_valor)
                                print("✅ Título atualizado!")
                            case "2":
                                novo_valor = input("Nova descrição: ")
                                manager.editar_tarefa(tarefa_idx, "descricao", novo_valor)
                                print("✅ Descrição atualizada!")
                            case "3":
                                while True:
                                    novo_valor = input("Nova prioridade [baixa/média/alta]: ")
                                    if novo_valor in ["baixa", "média", "alta"]:
                                        manager.editar_tarefa(tarefa_idx, "prioridade", novo_valor)
                                        print("✅ Prioridade atualizada!")
                                        break
                                    print("❌ Prioridade inválida!")
                            case "4":
                                print(f"Tem certeza que deseja marcar a tarefa {manager.tarefas[tarefa_idx].titulo} como concluida?")
                                resposta = input("\nDigite [S] para sim e [N] para não: ").upper()
                                if resposta == "S":
                                    manager.marcar_concluida(tarefa_idx)
                                    print(f"Tarefa{manager.tarefas[tarefa_idx].titulo} atualizada para concluida")
                                elif resposta == "N":
                                    print("Operação cancelada")
                                else:
                                    print("Digite [S] ou [N]")
                                break

                            case "5":
                                print("Saindo...")
                                break

                            case _:
                                print("❌ Opção inválida!")

                    except ValueError:
                        print("❌ Digite um número válido!")

            case "5":
                print("\n👋 Até logo!")
                break

            case _:
                print("\n❌ Opção inválida!")


if __name__ == "__main__":
    main()
