#arquivo Taks

import datetime
class Task:
    def __init__(self, titulo, descricao, prioridade, status = "Em andamento"):
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.status = status
        self.data_criacao = datetime.datetime.now()

    def __str__(self):
        return (
            f"Tarefa: {self.titulo}\n"
            f"Descrição: {self.descricao}\n"
            f"Prioridade: {self.prioridade}\n"
            f"Status: {self.status}\n"
            f"Criada em: {self.data_criacao.strftime('%d/%m/%Y %H:%M')}"
        )

