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

## 🚀 Se você fosse lançar esse gerenciador de animes no mercado, **o modelo de negócios ideal seria:**

### 🧩 **Modelo Freemium com Monetização Múltipla**

Oferece um app/site gratuito com funcionalidades básicas e cobra por recursos avançados. Isso permite atrair um grande público e converter uma parte em clientes pagantes.

### 🔹 Plano Gratuito

Inclui:

- Adicionar animes à lista de “quero assistir”
- Marcar como assistido
- Ver listas criadas
- Adicionar manualmente animes que não estão cadastrado.

### 🔸 Plano Premium (Assinatura mensal ou trimestral)

Inclui:

- Recomendação automática de animes com base no histórico
- Lista de "animes populares no momento.
- Estatísticas detalhadas (tempo assistido, categorias favoritas, etc.)
- Remoção de anúncios

**Preço sugerido:**

- R$ 9,90/mês
- R$ 25,90/trimestral

### 🧠 Por que esse modelo?

- O público otaku costuma valorizar **personalização**, **estatísticas** e **organização**.
- Muitos não querem pagar logo de cara, mas estão dispostos a pagar por **conforto e recursos legais**.
- O modelo freemium é ideal para escalar e validar rápido no início.

## 📣 Como atrair os primeiros usuários para seu gerenciador de animes

### 🎯 1. **Defina seu público com clareza**

Você está mirando principalmente em:

- **Fãs de anime** (otakus iniciantes e experientes)
- Usuários que consomem conteúdo em plataformas como Crunchyroll, Anilist, MyAnimeList, YouTube, TikTok, etc.
- Pessoas que gostam de organização e produtividade

---

### 🚪 2. **Canais e Estratégias de Aquisição**

### 🔹 A. **Comunidades otaku**

- Poste em grupos de **Facebook, Discord, Reddit e Telegram** voltados para animes
- Peça feedback em troca de recursos premium grátis por 1 mês

---

### 🔹 B. **TikTok e Instagram Reels**

- Faça vídeos curtos mostrando:
    - “Como organizo meus animes com esse app”
    - “Top 5 animes que organizei essa semana”
    - “Melhor app para quem assiste anime toda hora!”

## 📊 Estimativa de CAC – **SEM considerar tempo como custo**

### 🎯 Cenário:

- Grava vídeos no TikTok, Instagram e YouTube Shorts
- Não paga anúncios nem terceiriza nada
- Atrai 100 usuários por mês

### ✅ Cálculo:

CAC= R$/100 cliente = 0

## 📊 Estimativa de CAC – **COM tempo como custo **

### 🎯 Cenário:

- Produz **2 vídeos por semana**
- Cada vídeo leva **2 horas** para gravar e editar
- 1 mês = 8 vídeos → 16 horas
- Valor estimado da sua hora de trabalho: **R$ 20**
- Resultado: atraiu **100 usuários**

### ✅ Cálculo:

Custo total = 16 horas * 20 reais = 320 reais

CAC= 320/100 cliente = 3,20 reias p/ cliente

| Modelo | Custo investido | Clientes adquiridos | CAC estimado |
| --- | --- | --- | --- |
| **Sem considerar tempo** | R$ 0 | 100 | **R$ 0** |
| **Considerando tempo (realista)** | R$ 320 (em tempo) | 100 | **R$ 3,20** |

## 📊 LTV, Cenário base

**Preço:**

- Plano mensal: R$ 9,90
- Plano trimestral: R$ 25,90 (equivale a R$ 8,63/mês)

**Suposição:**

- 60% escolhem o mensal, 40% o trimestral
- Tempo médio de permanência: entre 6 e 12 meses

🧮 1. **Cálculo da receita média mensal por cliente (ARPU)**

ARPU=(60%×R$9,90)+(40%×R$8,63)=R$9,36

🧮 2. **LTV com base em diferentes tempos de retenção**

| Tempo médio (em meses) | LTV estimado (ARPU x tempo) |
| --- | --- |
| 6 meses | R$ 9,36 × 6 = **R$ 56,16** |
| 9 meses | R$ 9,36 × 9 = **R$ 84,24** |
| 12 meses | R$ 9,36 × 12 = **R$ 112,32** |

## 🎯 Resultado final

**👉 LTV estimado: entre R$ 56 e R$ 112 por cliente**

## 💡 Como **maximizar o LTV**

Para aumentar o valor que cada cliente gera ao longo do tempo:

### 1. **Aumentar retenção**

- Enviar notificações com lembretes: “Você ainda quer assistir Naruto?”
- Criar metas semanais e progressos.
- Ter um sistema de “animes concluídos” e “em andamento” para manter o engajamento

### 2. **Upsell ou plano anual**

- Criar um plano anual com desconto: R$ 79,90/ano (~R$ 6,66/mês)

### 3. **Adicionar recursos premium**

- Listas personalizadas ilimitadas
- Estatísticas de horas assistidas

### 4. **Sistema de pontos ou conquistas**

- Recompensas por concluir temporadas
- Medalhas de quantidade assistidas.

# 💰 Estratégias de monetização

## 💰 **Modelo Freemium (Grátis + Premium)**

### Como funciona:

- **Versão gratuita** com funções básicas (ex: criar lista, marcar como assistido)
 🧩 1. **Google AdSense** (para site)
Mostra anúncios contextuais no seu site.

Ganha por:

CPC (Custo por clique): quando o usuário clica no anúncio

CPM (Custo por mil impressões): quando o anúncio é exibido 1.000 vezes (mesmo sem clique)

📱 2. **Google AdMob** (para app mobile Android/iOS)
Permite banners, intersticiais (anúncios entre ações), e vídeos com recompensa.

Você ganha por:

Cliques

Visualizações (em vídeo)

Usuários que assistem vídeos até o fim (mais valioso)

**📊 Quanto se ganha por anúncios?**

| Tipo de Anúncio           | Ganho Estimado               |
| ------------------------- | ---------------------------- |
| **CPC (clique)**          | R\$ 0,10 a R\$ 0,50          |
| **CPM (mil impressões)**  | R\$ 2,00 a R\$ 5,00          |
| **Vídeos com recompensa** | R\$ 0,10 a R\$ 0,30 por view |


- **Versão premium** com recursos avançados:
    - Lista ilimitada
    - Estatísticas de animes assistidos
    - Temas customizados
    - Conquistas/gamificação


### Vantagens:

- Atrai muitos usuários gratuitamente
- Converte uma parte em assinantes pagos

### Preço:

- R$ 9,90/mês ou R$ 25,90/trimestre

## 🔐 Estratégias de retenção

### ✅ 1. **Gamificação**

- 🎖️ Pontos por animes marcados como assistidos
- 🏅 Conquistas como “Maratonador”, “Otaku Clássico”, “Explorer de Gêneros”
- 📊 Rankings entre amigos: “Quem assistiu mais esse mês?”
- 🎯 Missões semanais: “Adicione 3 novos animes à sua lista esta semana”

> Objetivo: transformar a experiência em algo recompensador e divertido.
> 

### ✅ 2. **Customização da experiência**

- 🎨 Temas personalizados (claro/escuro, cores de fundo)
- 🧩 Avatares de personagens e perfis editáveis
- 🧾 Organização de listas por categoria: “Shounen”, “Slice of Life”, “Favoritos”

> Objetivo: dar ao usuário sensação de posse e identidade.
> 

### ✅ 3. **Notificações inteligentes**

- 🔔 Lembretes de episódios lançados (para animes em andamento)
- 📅 Sugestões personalizadas: “Você gostou de Jujutsu Kaisen. Que tal Chainsaw Man?”
- ⏰ Alertas semanais: “Você não atualiza sua lista há 7 dias!”

> Objetivo: manter o app presente na rotina do usuário sem ser invasivo.
>
