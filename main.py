import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    """Carrega as tarefas do arquivo JSON."""
    if not os.path.exists(TASKS_FILE):
        return []
    try:
        with open(TASKS_FILE, 'r', encoding='utf-8') as f:
            tasks = json.load(f)
            return tasks
    except (json.JSONDecodeError, IOError) as e:
        print(f"Erro ao carregar as tarefas: {e}")
        return [] # Retorna lista vazia se houver erro ou o arquivo estiver vazio/mal formatado

def save_tasks(tasks):
    """Salva a lista de tarefas no arquivo JSON."""
    try:
        with open(TASKS_FILE, 'w', encoding='utf-8') as f:
            json.dump(tasks, f, indent=2, ensure_ascii=False)
    except IOError as e:
        print(f"Erro ao salvar as tarefas: {e}")

def display_tasks(tasks):
    """Exibe a lista de tarefas de forma organizada."""
    if not tasks:
        print("Nenhuma tarefa encontrada.")
        return

    print("\n--- Lista de Tarefas ---")
    for task in tasks:
        print(f"  ID: {task.get('id')}")
        print(f"  Título: {task.get('title')}")
        print(f"  Status: {task.get('status')}")
        print(f"  Data de Entrega: {task.get('dueDate')}")
        print("  --------------------")

def add_task(tasks):
    """Adiciona uma nova tarefa à lista."""
    print("\n--- Adicionar Nova Tarefa ---")
    title = input("Digite o título da tarefa: ")
    dueDate = input("Digite a data de entrega (ex: AAAA-MM-DD): ")

    # Gerar novo ID
    new_id = 1
    if tasks:
        # Encontra o maior ID existente e adiciona 1
        # Certifique-se de que todos os IDs são inteiros para max() funcionar corretamente
        # ou filtre/converta IDs não numéricos se necessário.
        ids = [task.get('id', 0) for task in tasks if isinstance(task.get('id'), int)]
        if ids: # se houver IDs numéricos
            new_id = max(ids) + 1
        # Se não houver IDs numéricos (ex: lista vazia ou tasks com IDs não-int), new_id continua 1

    new_task = {
        "id": new_id,
        "title": title,
        "status": "pending",
        "dueDate": dueDate
    }
    tasks.append(new_task)
    print(f"Tarefa \'{title}\' adicionada com sucesso!")

def mark_task_done(tasks):
    """Marca uma tarefa como concluída."""
    print("\n--- Marcar Tarefa como Concluída ---")
    display_tasks(tasks) # Mostrar tarefas para o usuário saber o ID
    if not tasks:
        return # Se não há tarefas, não há nada a fazer

    try:
        task_id_str = input("Digite o ID da tarefa que deseja marcar como concluída: ")
        task_id = int(task_id_str)
    except ValueError:
        print("ID inválido. Por favor, digite um número.")
        return

    task_found = False
    for task in tasks:
        if task.get('id') == task_id:
            task['status'] = "done"
            print(f"Tarefa '{task.get('title')}' (ID: {task_id}) marcada como concluída!")
            task_found = True
            break
    
    if not task_found:
        print(f"Tarefa com ID {task_id} não encontrada.")

def delete_task(tasks):
    """Exclui uma tarefa da lista."""
    print("\n--- Excluir Tarefa ---")
    display_tasks(tasks)
    if not tasks:
        return

    try:
        task_id_str = input("Digite o ID da tarefa que deseja excluir: ")
        task_id = int(task_id_str)
    except ValueError:
        print("ID inválido. Por favor, digite um número.")
        return

    original_task_count = len(tasks)
    # Usamos uma compreensão de lista para recriar a lista sem a tarefa a ser excluída
    # Isso é mais seguro do que modificar a lista enquanto iteramos sobre ela
    tasks_to_keep = [task for task in tasks if task.get('id') != task_id]
    
    if len(tasks_to_keep) < original_task_count:
        # Atualiza a lista original de tarefas. Precisamos fazer isso de forma a modificar
        # a lista original que foi passada como argumento, e não criar uma nova local.
        tasks.clear() # Remove todos os itens da lista original
        tasks.extend(tasks_to_keep) # Adiciona todos os itens da lista filtrada
        print(f"Tarefa com ID {task_id} excluída com sucesso!")
    else:
        print(f"Tarefa com ID {task_id} não encontrada.")

def update_task(tasks):
    """Atualiza uma tarefa existente (título ou data de entrega)."""
    print("\n--- Atualizar Tarefa ---")
    display_tasks(tasks)
    if not tasks:
        return

    try:
        task_id_str = input("Digite o ID da tarefa que deseja atualizar: ")
        task_id = int(task_id_str)
    except ValueError:
        print("ID inválido. Por favor, digite um número.")
        return

    task_to_update = None
    for task in tasks:
        if task.get('id') == task_id:
            task_to_update = task
            break

    if not task_to_update:
        print(f"Tarefa com ID {task_id} não encontrada.")
        return

    print(f"Atualizando tarefa: '{task_to_update.get('title')}' (ID: {task_id})")
    print("O que você deseja atualizar?")
    print("1. Título")
    print("2. Data de Entrega")
    print("0. Cancelar")
    
    update_choice = input("Escolha uma opção: ")

    if update_choice == '1':
        new_title = input("Digite o novo título: ")
        task_to_update['title'] = new_title
        print("Título atualizado com sucesso!")
    elif update_choice == '2':
        new_dueDate = input("Digite a nova data de entrega (AAAA-MM-DD): ")
        task_to_update['dueDate'] = new_dueDate
        print("Data de entrega atualizada com sucesso!")
    elif update_choice == '0':
        print("Atualização cancelada.")
    else:
        print("Opção de atualização inválida.")

def main():
    """Função principal da aplicação."""
    tasks = load_tasks()

    while True:
        print("\n--- Menu Principal ---")
        print("1. Listar tarefas")
        print("2. Adicionar nova tarefa")
        print("3. Marcar tarefa como concluída")
        print("4. Excluir tarefa")
        print("5. Atualizar tarefa")
        # Adicionaremos mais opções aqui no futuro (atualizar, deletar, etc.)
        print("0. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
            save_tasks(tasks) # Salva após adicionar uma nova tarefa
        elif choice == '3':
            mark_task_done(tasks)
            save_tasks(tasks) # Salva após modificar uma tarefa
        elif choice == '4':
            delete_task(tasks)
            save_tasks(tasks) # Salva após excluir uma tarefa
        elif choice == '5':
            update_task(tasks)
            save_tasks(tasks) # Salva após atualizar uma tarefa
        elif choice == '0':
            print("Saindo do gerenciador de tarefas. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main() 