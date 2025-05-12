# Para iniciar o projeto basta abrir o terminal e digitar

python main.py

Que o projeto sera inicializado.


# **Decisões Técnicas e Foco na Experiência do Usuário (UX)**
## Ao desenvolver o Gerenciador de Tarefas, diversas decisões técnicas foram feitas com o objetivo de criar uma aplicação funcional, de fácil manutenção e, com uma boa experiência para o usuário final.

**Linguagem**: Python foi escolhido devido à facilidade em codar, e por ser excelente para o desenvolvimento rápido de aplicações.

**Funções**: O código foi dividido em funções para cada responsabilidade principal (carregar/salvar tarefas, exibir tarefas, adicionar, marcar como concluída, excluir, atualizar). 

# Foco na Experiência do Usuário (UX)

### Menu Interativo:
Um menu principal com opções é apresentado ao usuário, guiando pelas funções disponíveis.

### Feedback Claro e Consistente:

**Prompts**: As solicitações de entrada de dados como: ("Digite o nome da tarefa:", "Escolha uma opção:") são claras e diretas.

**Confirmações**: Após cada operação for bem-sucedida (adicionar, concluir, excluir, atualizar), uma mensagem de sucesso é exibida, confirmando para o usuário.

**Mensagens de Erro**: Erros de entrada (como um ID não numérico) ou operacionais (como tentar operar sobre uma tarefa com ID inexistente) são comunicados de forma compreensível, orientando o usuário sobre o problema.

## Uso de Cores para Melhorar a visualização:

**Para destacar as informações importantes e melhorar visualmente, foram implementadas cores no terminal**:

**Azul (Colors.BLUE)**: Usado para cabeçalhos de seção, opções de menu, prompts de entrada e rótulos de informações (como "ID:", "Título:"), ajudando a guiar o olhar do usuário.

**Verde (Colors.GREEN)**: Usado para todas as mensagens de sucesso e para indicar tarefas "Concluídas", fornecendo um feedback visual positivo.

**Vermelho (Colors.RED)**: Usado para todas as mensagens de erro, alertas (como tarefa já concluída ao tentar marcar novamente) e para indicar tarefas "Pendentes", chamando a atenção para problemas ou status que requerem ação.

**Reset (Colors.RESET)**: Garante que a cor seja redefinida para o padrão do terminal após cada mensagem colorida, evitando que a formatação "vaze" para outras saídas.

## Exibição Organizada das Tarefas:
A função exibir_tarefas formata a lista de tarefas de maneira clara, mostrando ID, Título, Status (com um indicador visual como ✅ ou ⏳ e cor) e Data de Entrega. Facilitando a visualização e a identificação das tarefas para as operações seguintes.

**Validação de Entrada**:
Validações básicas, como verificar se o ID fornecido é um número e ao adicionar tarefas, verifica-se se o nome não está vazio.

# Video:
https://files.fm/u/axdhpcx9ns

# **📦 Modelo de Negócios**

**Gratuito**: funcionalidades como adicionar/gerenciar listas e marcar como assistido.

**Premium**: recursos como:

Recomendação de animes com base no perfil

Temas personalizados

Melhor qualidade de streaming

# **🚀 Estratégia para Atrair Primeiros Usuários**

## **Canais e táticas**:

**Redes Sociais e Comunidades**: usar Twitter (X), TikTok e Reddit com conteúdos , como listas "Top 10 animes para assistir em 2025", memes e reviews.

**Parcerias com Influencers**: influenciadores otakus que podem apresentar o app como útil e divertido.

# 📊 **Estimativa de CAC (Custo de Aquisição de Cliente)**

**Ads iniciais em redes sociais**: R$ 0,50 a R$ 1,50 por clique.

**Conversão estimada**: 5% a 10% para instalações.

**CAC inicial médio**: R$ 10 a R$ 15 por usuário, podendo cair para R$ 5 ou menos com engajamento orgânico (via viralização e comunidades).

# **💰 Proposta de LTV (Lifetime Value)**

**Plano Premium mensal**: R$ 9,90

**Plano trimestral**: R$ 15,90

**Suposição de retenção média**: 6 a 12 meses
  
**LTV estimado**: R$ 60 a R$ 100 por usuário premium.

## **Como aumentar o LTV**:

Cross-sell com lojas de produtos otaku

Acesso antecipado a novas features para usuários pagantes

# **📈 Estratégias de Retenção**

**Gamificação**: pontos por episódios assistidos, conquistas por maratonas, ranking de tempo assistido.

Aviso de novos animes

Sugestões baseadas nos gostos do usuário



