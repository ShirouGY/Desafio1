import json
import os
import datetime # Adicionado para validação de data

ARQUIVO_TAREFAS = "tasks.json"
STATUS_PENDENTE = "pendente"
STATUS_CONCLUIDA = "concluída"

def carregar_tarefas():
    """Carrega as tarefas do arquivo JSON."""
    if not os.path.exists(ARQUIVO_TAREFAS):
        return []
    try:
        with open(ARQUIVO_TAREFAS, 'r', encoding='utf-8') as f:
            tarefas = json.load(f)
            # Validação básica para garantir que temos uma lista de dicionários
            if not isinstance(tarefas, list) or not all(isinstance(t, dict) for t in tarefas):
                print("Formato de arquivo de tarefas inválido. Iniciando com lista vazia.")
                return []
            return tarefas
    except (json.JSONDecodeError, IOError) as e:
        print(f"Erro ao carregar as tarefas: {e}. Iniciando com lista vazia.")
        return []

def salvar_tarefas(tarefas):
    """Salva a lista de tarefas no arquivo JSON."""
    try:
        with open(ARQUIVO_TAREFAS, 'w', encoding='utf-8') as f:
            json.dump(tarefas, f, indent=2, ensure_ascii=False)
    except IOError as e:
        print(f"Erro ao salvar as tarefas: {e}")

def _validar_formato_data(data_str):
    """Valida se a string da data está no formato AAAA-MM-DD."""
    try:
        datetime.datetime.strptime(data_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def exibir_tarefas(tarefas):
    """Exibe a lista de tarefas de forma organizada."""
    if not tarefas:
        print("\nNenhuma tarefa cadastrada ainda.")
        return

    print("\n--- Sua Lista de Tarefas ---")
    for tarefa in tarefas:
        status_legivel = "Concluída ✅" if tarefa.get('status') == STATUS_CONCLUIDA else "Pendente ⏳"
        data_entrega = tarefa.get('dueDate') or "Não definida"
        print(f"  ID: {tarefa.get('id')}")
        print(f"  Título: {tarefa.get('title')}")
        print(f"  Status: {status_legivel}")
        print(f"  Data de Entrega: {data_entrega}")
        print("  --------------------")

def adicionar_tarefa(tarefas):
    """Adiciona uma nova tarefa à lista."""
    print("\n--- Adicionar Nova Tarefa ---")
    titulo = input("Qual o título da tarefa? ").str0ip()
    if not titulo:
        print("O título não pode ser vazio. Tarefa não adicionada.")
        return

    while True:
        data_entrega_str = input("Qual a data de entrega (AAAA-MM-DD, deixe em branco se não houver)? ").strip()
        if not data_entrega_str or _validar_formato_data(data_entrega_str):
            break
        print("Formato de data inválido. Por favor, use AAAA-MM-DD ou deixe em branco.")

    novo_id = 1
    if tarefas:
        ids_existentes = [t.get('id', 0) for t in tarefas if isinstance(t.get('id'), int)]
        if ids_existentes:
            novo_id = max(ids_existentes) + 1

    nova_tarefa = {
        "id": novo_id,
        "title": titulo,
        "status": STATUS_PENDENTE,
        "dueDate": data_entrega_str if data_entrega_str else None
    }
    tarefas.append(nova_tarefa)
    print(f"\nTarefa '{titulo}' adicionada com sucesso! ID: {novo_id}")

def _obter_id_tarefa_do_usuario(mensagem_prompt="Digite o ID da tarefa: "):
    """Solicita ao usuário um ID de tarefa e garante que seja um número."""
    while True:
        try:
            id_str = input(mensagem_prompt)
            return int(id_str)
        except ValueError:
            print("ID inválido. Por favor, digite um número.")

def _encontrar_tarefa_por_id(tarefas, id_tarefa):
    """Encontra uma tarefa na lista pelo seu ID."""
    for tarefa in tarefas:
        if tarefa.get('id') == id_tarefa:
            return tarefa
    return None

def marcar_tarefa_concluida(tarefas):
    """Marca uma tarefa como concluída."""
    print("\n--- Marcar Tarefa como Concluída ---")
    if not tarefas:
        print("Nenhuma tarefa para marcar.")
        return

    exibir_tarefas(tarefas) # Mostrar tarefas para facilitar a escolha do ID
    id_tarefa = _obter_id_tarefa_do_usuario("Digite o ID da tarefa para marcar como concluída: ")

    tarefa = _encontrar_tarefa_por_id(tarefas, id_tarefa)

    if tarefa:
        if tarefa['status'] == STATUS_CONCLUIDA:
            print(f"A tarefa '{tarefa.get('title')}' (ID: {id_tarefa}) já estava marcada como concluída.")
        else:
            tarefa['status'] = STATUS_CONCLUIDA
            print(f"Tarefa '{tarefa.get('title')}' (ID: {id_tarefa}) marcada como concluída! 🎉")
    else:
        print(f"Tarefa com ID {id_tarefa} não encontrada. 🤔")

def excluir_tarefa(tarefas):
    """Exclui uma tarefa da lista."""
    print("\n--- Excluir Tarefa ---")
    if not tarefas:
        print("Nenhuma tarefa para excluir.")
        return

    exibir_tarefas(tarefas)
    id_tarefa = _obter_id_tarefa_do_usuario("Digite o ID da tarefa que deseja excluir: ")

    tarefa = _encontrar_tarefa_por_id(tarefas, id_tarefa)

    if tarefa:
        confirmacao = input(f"Tem certeza que deseja excluir a tarefa '{tarefa.get('title')}' (ID: {id_tarefa})? (s/N): ").strip().lower()
        if confirmacao == 's':
            tarefas.remove(tarefa) # Mais direto se o objeto tarefa é o correto
            print(f"Tarefa '{tarefa.get('title')}' excluída com sucesso! 👍")
        else:
            print("Exclusão cancelada.")
    else:
        print(f"Tarefa com ID {id_tarefa} não encontrada.")


def atualizar_tarefa(tarefas):
    """Atualiza o título ou a data de entrega de uma tarefa existente."""
    print("\n--- Atualizar Tarefa ---")
    if not tarefas:
        print("Nenhuma tarefa para atualizar.")
        return

    exibir_tarefas(tarefas)
    id_tarefa = _obter_id_tarefa_do_usuario("Digite o ID da tarefa que deseja atualizar: ")

    tarefa_para_atualizar = _encontrar_tarefa_por_id(tarefas, id_tarefa)

    if not tarefa_para_atualizar:
        print(f"Tarefa com ID {id_tarefa} não encontrada.")
        return

    print(f"\nAtualizando tarefa: '{tarefa_para_atualizar.get('title')}' (ID: {id_tarefa})")
    print("Deixe o campo em branco se não quiser alterar o valor atual.")

    novo_titulo = input(f"Novo título (atual: '{tarefa_para_atualizar.get('title')}'): ").strip()
    if novo_titulo:
        tarefa_para_atualizar['title'] = novo_titulo
        print("Título atualizado!")

    while True:
        nova_data_entrega_str = input(f"Nova data de entrega (AAAA-MM-DD, atual: '{tarefa_para_atualizar.get('dueDate') or 'Não definida'}'): ").strip()
        if not nova_data_entrega_str: # Usuário deixou em branco, não altera
            break
        if _validar_formato_data(nova_data_entrega_str):
            tarefa_para_atualizar['dueDate'] = nova_data_entrega_str
            print("Data de entrega atualizada!")
            break
        print("Formato de data inválido. Por favor, use AAAA-MM-DD ou deixe em branco para não alterar.")
    
    if not novo_titulo and not (nova_data_entrega_str and _validar_formato_data(nova_data_entrega_str)): # Verifica se algo foi realmente alterado
        print("Nenhuma alteração realizada.")
    else:
        print("\nTarefa atualizada com sucesso!")

def main():
    """Função principal da aplicação de gerenciamento de tarefas."""
    tarefas = carregar_tarefas()

    print("Bem-vindo ao seu Gerenciador de Tarefas Pessoal! 🚀")

    while True:
        print("\n--- Menu Principal ---")
        print("1. Listar tarefas")
        print("2. Adicionar nova tarefa")
        print("3. Marcar tarefa como concluída")
        print("4. Atualizar tarefa")
        print("5. Excluir tarefa")
        print("0. Sair")

        escolha = input("O que você gostaria de fazer? Escolha uma opção: ")

        if escolha == '1':
            exibir_tarefas(tarefas)
        elif escolha == '2':
            adicionar_tarefa(tarefas)
            salvar_tarefas(tarefas)
        elif escolha == '3':
            marcar_tarefa_concluida(tarefas)
            salvar_tarefas(tarefas)
        elif escolha == '4':
            atualizar_tarefa(tarefas)
            salvar_tarefas(tarefas)
        elif escolha == '5':
            excluir_tarefa(tarefas)
            salvar_tarefas(tarefas)
        elif escolha == '0':
            print("\nObrigado por usar o Gerenciador de Tarefas! Até a próxima! 👋")
            break
        else:
            print("Opção inválida. Por favor, escolha um número do menu.")

if __name__ == "__main__":
    main()