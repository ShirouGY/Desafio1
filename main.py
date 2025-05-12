import json
import os
import datetime 

class Colors:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'

ARQUIVO_TAREFAS = "tasks.json"
STATUS_CONCLUIDA = "concluída"

def carregar_tarefas():
    if not os.path.exists(ARQUIVO_TAREFAS):
        return []
    try:
        with open(ARQUIVO_TAREFAS, 'r', encoding='utf-8') as file:
            tarefas = json.load(file)
            if not isinstance(tarefas, list) or not all(isinstance(t, dict) for t in tarefas): ## verificar com IA
                print(f"{Colors.RED}Formato de arquivo vazio.{Colors.RESET}")
                return []
            return tarefas
    except (json.JSONDecodeError, IOError) as e:
        print(f"{Colors.RED}Erro ao carregar as tarefas: {e}.{Colors.RESET}")
        return []

def salvar_tarefas(tarefas):
    try:
        with open(ARQUIVO_TAREFAS, 'w', encoding='utf-8') as file:
            json.dump(tarefas, file, indent=2, ensure_ascii=False)
    except IOError as e:
        print(f"{Colors.RED}Erro ao salvar as tarefas: {e}{Colors.RESET}")

def validar_formato_da_data(data_str):
    try:
        datetime.datetime.strptime(data_str, '%Y-%m-%d') ## pq datetime.datetime.strptime?
        return True
    except ValueError:
        return False

def exibir_tarefas(tarefas):
    if not tarefas:
        print(f"{Colors.BLUE}Nenhuma tarefa cadastrada ainda.{Colors.RESET}")
        return

    print(f"\n{Colors.BLUE}--- Sua Lista de Tarefas ---{Colors.RESET}")
    for tarefa in tarefas:
        status_legivel = f"{Colors.GREEN}Concluída ✅{Colors.RESET}" if tarefa.get('status') == STATUS_CONCLUIDA else f"{Colors.RED}Pendente ⏳{Colors.RESET}"
        data_entrega = tarefa.get('dueDate') or "Não definida"
        print(f"  ID: {tarefa.get('id')}")
        print(f"  Nome: {tarefa.get('nome')}")
        print(f"  Status: {status_legivel}")
        print(f"  Data de Entrega: {data_entrega}")
        print("  --------------------")

def adicionar_tarefa(tarefas):
    print(f"\n{Colors.BLUE}--- Adicionar Nova Tarefa ---{Colors.RESET}")
    nome = input(f"{Colors.BLUE}Qual o nome da tarefa? {Colors.RESET}").strip()
    if not nome:
        print(f"{Colors.RED}O nome não pode ser vazio. Tarefa não adicionada.{Colors.RESET}")
        return

    while True:
        data_entrega_str = input(f"{Colors.BLUE}Qual a data de entrega (AAAA-MM-DD, deixe em branco se não houver)? {Colors.RESET}").strip()
        if not data_entrega_str or validar_formato_da_data(data_entrega_str):
            break
        print(f"{Colors.RED}Formato de data inválido. Por favor, use AAAA-MM-DD ou deixe em branco.{Colors.RESET}")

    novo_id = 1
    if tarefas:
        ids_existentes = [t.get('id', 0) for t in tarefas if isinstance(t.get('id'), int)]  ## como explicar isso
        if ids_existentes:
            novo_id = max(ids_existentes) + 1

    nova_tarefa = {
        "id": novo_id,
        "nome": nome,
        "status": "pendente",
        "dueDate": data_entrega_str if data_entrega_str else None
    }
    tarefas.append(nova_tarefa)
    print(f"{Colors.GREEN}Tarefa '{nome}' adicionada com sucesso! ID: {novo_id}{Colors.RESET}")

def obter_id_tarefa_do_usuario(mensagem="Digite o ID da tarefa: "):
    while True:
        try:
            id_str = input(mensagem)
            return int(id_str)
        except ValueError:
            print(f"{Colors.RED}ID inválido. Por favor, digite um número.{Colors.RESET}")

def encontrar_tarefa_por_id(tarefas, id_tarefa):
    for tarefa in tarefas:
        if tarefa.get('id') == id_tarefa:
            return tarefa
    return None

def marcar_tarefa_concluida(tarefas):
    print(f"\n{Colors.BLUE}--- Marcar Tarefa como Concluída ---{Colors.RESET}")
    if not tarefas:
        print(f"{Colors.BLUE}Nenhuma tarefa para marcar.{Colors.RESET}")
        return

    exibir_tarefas(tarefas)
    id_tarefa = obter_id_tarefa_do_usuario("Digite o ID da tarefa para marcar como concluída: ")

    tarefa = encontrar_tarefa_por_id(tarefas, id_tarefa)

    if tarefa:
        if tarefa['status'] == STATUS_CONCLUIDA:
            print(f"{Colors.RED}A tarefa '{tarefa.get('nome')}' (ID: {id_tarefa}) já estava concluída.{Colors.RESET}")
        else:
            tarefa['status'] = STATUS_CONCLUIDA
            print(f"{Colors.GREEN}Tarefa '{tarefa.get('nome')}' (ID: {id_tarefa}) concluída! 🎉{Colors.RESET}")
    else:
        print(f"{Colors.RED}Tarefa com ID {id_tarefa} não encontrada. 🤔{Colors.RESET}")

def excluir_tarefa(tarefas):
    print(f"\n{Colors.BLUE}--- Excluir Tarefa ---{Colors.RESET}")
    if not tarefas:
        print(f"{Colors.BLUE}Nenhuma tarefa para excluir.{Colors.RESET}")
        return

    exibir_tarefas(tarefas)
    id_tarefa = obter_id_tarefa_do_usuario("Digite o ID da tarefa que deseja excluir: ")

    tarefa = encontrar_tarefa_por_id(tarefas, id_tarefa)

    if tarefa:
        confirmacao = input(f"{Colors.BLUE}Tem certeza que deseja excluir a tarefa '{tarefa.get('title')}' (ID: {id_tarefa})? (s/N): {Colors.RESET}").lower()
        if confirmacao == 's':
            tarefas.remove(tarefa)
            print(f"{Colors.GREEN}Tarefa '{tarefa.get('title')}' excluída com sucesso! 👍{Colors.RESET}")
        else:
            print(f"{Colors.BLUE}Exclusão cancelada.{Colors.RESET}")
    else:
        print(f"{Colors.RED}Tarefa com ID {id_tarefa} não encontrada.{Colors.RESET}")


def atualizar_tarefa(tarefas):
    print(f"\n{Colors.BLUE}--- Atualizar Tarefa ---{Colors.RESET}")
    if not tarefas:
        print(f"{Colors.BLUE}Nenhuma tarefa para atualizar.{Colors.RESET}")
        return

    exibir_tarefas(tarefas)
    id_tarefa = obter_id_tarefa_do_usuario("Digite o ID da tarefa para atualizar: ")

    tarefa_para_atualizar = encontrar_tarefa_por_id(tarefas, id_tarefa)

    if not tarefa_para_atualizar:
        print(f"{Colors.RED}Tarefa com ID {id_tarefa} não encontrada.{Colors.RESET}")
        return

    print(f"{Colors.BLUE}Atualizando tarefa: '{tarefa_para_atualizar.get('title')}' (ID: {id_tarefa}){Colors.RESET}")
    print(f"{Colors.BLUE}Deixe o campo em branco se não quiser alterar o valor atual.{Colors.RESET}")

    novo_nome = input(f"{Colors.BLUE}Novo nome (atual: '{tarefa_para_atualizar.get('title')}'): {Colors.RESET}").strip()
    if novo_nome:
        tarefa_para_atualizar['title'] = novo_nome
        print(f"{Colors.GREEN}Nome atualizado!{Colors.RESET}")

    while True:
        nova_data_entrega_str = input(f"{Colors.BLUE}Nova data de entrega (AAAA-MM-DD, atual: '{tarefa_para_atualizar.get('dueDate') or 'Não definida'}'): {Colors.RESET}").strip()
        if not nova_data_entrega_str:
            break
        if validar_formato_da_data(nova_data_entrega_str):
            tarefa_para_atualizar['dueDate'] = nova_data_entrega_str
            print(f"{Colors.GREEN}Data de entrega atualizada!{Colors.RESET}")
            break
        print(f"{Colors.RED}Formato de data inválido. Use AAAA-MM-DD ou deixe em branco para não alterar.{Colors.RESET}")
    
    if not novo_nome and not (nova_data_entrega_str and validar_formato_da_data(nova_data_entrega_str)):
        print(f"{Colors.BLUE}Nenhuma alteração realizada.{Colors.RESET}")
    else:
        print(f"{Colors.GREEN}Tarefa atualizada com sucesso!{Colors.RESET}")

def main():
    tarefas = carregar_tarefas()

    print(f"{Colors.BLUE}Bem-vindo ao seu Gerenciador de Tarefas! 🚀{Colors.RESET}")

    while True:
        print(f"\n{Colors.BLUE}--- Menu Principal ---{Colors.RESET}")
        print(f"{Colors.BLUE}1. Listar tarefas{Colors.RESET}")
        print(f"{Colors.BLUE}2. Adicionar nova tarefa{Colors.RESET}")
        print(f"{Colors.BLUE}3. Marcar tarefa como concluída{Colors.RESET}")
        print(f"{Colors.BLUE}4. Atualizar tarefa{Colors.RESET}")
        print(f"{Colors.BLUE}5. Excluir tarefa{Colors.RESET}")
        print(f"{Colors.BLUE}0. Sair{Colors.RESET}")

        escolha = input(f"{Colors.BLUE}Escolha uma opção: {Colors.RESET}")

        match escolha:
            case '1':
                exibir_tarefas(tarefas)
            case '2':
                adicionar_tarefa(tarefas)
                salvar_tarefas(tarefas)
            case '3':
                marcar_tarefa_concluida(tarefas)
                salvar_tarefas(tarefas)
            case '4':
                atualizar_tarefa(tarefas)
                salvar_tarefas(tarefas)
            case '5':
                excluir_tarefa(tarefas)
                salvar_tarefas(tarefas)
            case '0':
                print(f"{Colors.GREEN}Obrigado por usar o Gerenciador de Tarefas! Até a próxima! 👋{Colors.RESET}")
                break
            case _:
                print(f"{Colors.RED}Opção inválida. Por favor, escolha um número do menu.{Colors.RESET}")

if __name__ == "__main__":
    main()