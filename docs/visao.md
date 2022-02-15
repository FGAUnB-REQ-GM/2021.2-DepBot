# Visão do Produto e Projeto

## Histórico de Versões
|Data|Versão|Modificação|Autores|
|:---|:-----|:----------|:------|
|29/01/2022|0.1|Criação do documento|Lucas Braun, Pedro Lucas, Pedro Vieira, Victor Cabral, Vinicius Roriz|
|31/01/2022|0.2|Adição de novas informações nos tópicos do documento|Lucas Braun, Pedro Lucas, Pedro Vieira, Victor Cabral, Vinicius Roriz|
|02/02/2022|0.3|Revisão e melhoria nos textos|Lucas Braun, Pedro Lucas, Pedro Vieira, Victor Cabral, Vinicius Roriz|
|08/02/2022|0.4|Atualização na seção de Abordagem de Desenvolvimento de Software| Vinicius Roriz |
|09/02/2022|0.4.1| Atualização ref. bibliográficas e seção 1.3| Lucas Braun |
|11/02/2022|0.5|Adição do esqueleto das novas seções e especificação do tipo de deputado|Victor Cabral|
|11/02/2022|0.6|Revisão e mudança na seção de Verificação de Requisitos|Pedro Lucas|## 1. Visão Geral do Produto|
|11/02/2022|0.7|Revisão da seção de lições aprendidas | Lucas Braun e Vinicius Roriz |
|11/02/2022|0.8|Atualização na seção Organização do Projeto| Victor Cabral |
|13/02/2022|0.9|Adicionando matriz de comunicação| Lucas Braun |
|13/02/2022|0.10|Adicionando critérios de replanejamento| Vinicius Roriz |
14/02/2022|0.11|Adicionando requisitos funcionais e não funcionais| Vinicius Roriz |
15/02/2022|0.12|Adicionando MVP| Pedro Vieira e Victor Cabral |

## 1. Visão Geral
### 1.1 Declaração do Problema
| | |
|:-|:-|
|**O problema**|Com a dificuldade de acessibilidade das informações dos representantes políticos da Câmera do Deputados.|
|**Afeta**|A população eleitoral.|
|**Cujo impacto é**|Desinformação e, consequentemente, um voto infundado.|
|**Uma solução de sucesso seria**|Um bot que apresenta dados da Câmera dos Deputados ao usuário que utilizá-lo.|

### 1.2 Declaração de Posição do Produto

O DepBot é uma aplicação para a plataforma Telegram que visa agregar informações a respeito da Câmara dos Deputados, simulando uma conversa usual e natural com o usuário. A ideia é facilitar a acessibilidade dos dados disponibilizados e abertos pelo poder Legislativo que, apesar de estarem disponíveis para acesso a qualquer momento, acaba por ser uma tarefa de baixa praticidade. 

Logo, ao invés de navegar pela internet a procura dos dados, verificando a confiabilidade dos mesmos, o DepBot propõe uma solução mais eficiente e estimulante para a procura. As informações serão então consolidadas em uma conversa com um robô que busca ser intuitiva para o usuário do produto.

| | |
|:-|:-|
|**Para**|Cidadãos maiores de 16 anos.|
|**Que**|Não possuem informações o suficiente sobre os candidatos a deputado.|
|**O DepBot**|É um chatbot.|
|**Que**|Disponibiliza informações da Câmara dos Deputados aos usuários.|
|**Ao contrário**|De pesquisar individualmente as informações de cada candidato.|
|**Nosso produto**|Proporciona as informações diretamente no Telegram. |

### 1.3 Objetivos do Produto 

O objetivo do produto é fornecer informações sobre a Câmara dos Deputados à população eleitoral. Com o DepBot, o usuário poderá receber tanto informações básicas quanto despesas, frente parlamentar, partidos associados, ocupações, escolaridade, etc. do candidato que ele pesquisar sobre. Assim, aprendendo ou confirmando informações sobre o deputado, o que permite realizar um voto mais fundamentado. Além disso o bot também trará informações gerais sobre a Câmara dos Deputados, eleições e votações que ocorreram no plenário com intuito de infomar bem o usuário sobre esses tópicos.    

### 1.4	Escopo do Produto

### 1.4.1	Requisitos Funcionais

|Requisito|Épico|Descrição|
|--------|-----|---------|
|**RF1**| Deputados | Permitir a pesquisa de deputados federais que estão em exercício e ex-deputados federais |
|**RF2**| Deputados | Disponibilizar informações sobre o deputado como nome, partido, sexo, ocupações, profissões, votações e escolaridade |
|**RF3**| Deputados | Listar os partidos que têm ou já tiveram parlamentares em exercício na Câmara |
|**RF4**| Deputados | Pesquisar deputados por nome e sobrenome, partido e UF |
|**RF5**| Deputados | Disponibilizar informações sobre as despesas com exercício parlamentar do deputado |
|**RF6**| Deputados | Disponibilizar informações sobre as frentes parlamentares das quais o deputado é integrante |
|**RF7**| Informativo | Disponibilizar informações sobre as votações que ocorreram no plenário |
|**RF8**| Informativo | Apresentar informações sobre a Câmara dos Deputados |
|**RF9**| Informativo | Listar todas as UFs com siglas e nomes por extenso |
|**RF10**| Informativo | Disponibilizar informações sobre as eleições |
|**RF11**| Informativo | Definir e descrever os termos usados pela API dos Dados Abertos da Câmara dos Deputados |
|**RF12**| Sistema | Auxiliar através de comandos _/help_ e _/ajuda_ as possíveis funcionalidades do bot |
|**RF13**| Sistema | O software deve conversar casualmente com o usuário |
|**RF14**| Sistema | O software deve, em caso de falha na compreensão, demonstrar o não entendimento da solicitação do usuário |
|**RF15**| Sistema | Responder as saudações digitadas pelo usuário |

#### 1.4.2	Requisitos Não-Funcionais

|Requisito|Descrição|
|--------|---------|
|**RNF1** | A linguagem de programação usada será Python
|**RNF2** | O bot deverá conversar em português
|**RNF3** | O bot usa a API dos Dados Abertos da Câmara dos Deputados
|**RNF4** | O sistema não deve propagar informações falsas sobre os deputados, eleições e Câmara dos Deputados
**RNF5** | O software deve mostrar informações sem viés político

### 1.5	Mínimo Produto Viável (MVP)

|Requisito|Descrição|
|--------|---------|
|**RF1**| Permitir a pesquisa de deputados federais que estão em exercício e ex-deputados federais |
|**RF2**| Disponibilizar informações sobre o deputado como nome, partido, sexo, ocupações, profissões, votações e escolaridade |
|**RF3**| Listar os partidos na qual os deputados são associados |
|**RF8**| Apresentar informações sobre a Câmara dos Deputados |
|**RF9**| Listar todas as UFs com siglas e nomes por extenso |
|**RF11** | Definir e descrever os termos usados pela API dos Dados Abertos da Câmara dos Deputados |
|**RF12**| Auxiliar através de comandos _/help_ e _/ajuda_ as possíveis funcionalidades do bot |
|**RNF1** | A linguagem de programação usada será Python |
|**RNF2** | O bot deverá conversar em português |
|**RNF3** | O bot usa a API dos Dados Abertos da Câmara dos Deputados |
|**RNF4** | O sistema não deve propagar informações falsas sobre os deputados, eleições e Câmara dos Deputados |
|**RNF5** | O software deve mostrar informações sem viés político |

### 1.6	Organização dos requisitos conforme SAFe

<p align="center">
  <img src="https://github.com/FGAUnB-REQ-GM/2021.2-DepBot/blob/main/docs/assets/requisitosSAFe.jpg?raw=true">
</p>

## 2. Abordagem de Desenvolvimento de Software

Após cuidadosa consideração, a abordagem escolhida pelo time para o desenvolvimento do projeto foi o Cascata, devido à capacidade de estimar e prever o tempo e orçamento totais do projeto que ele proporciona, além de possuir etapas estruturadas e foco no planejamento. Sommerville informa que o Cascata deve ser usado apenas quando os requisitos são bem conhecidos e pouco prováveis de sofrerem alteração, e nesse aspecto o escopo do projeto condiz com a abordagem. Também serão utilizadas algumas práticas do XP, como a Propriedade Coletiva, que estipula que todos podem modificar o código a qualquer momento, e a Programação em Pares, que além de garantir uma maior qualidade de código e reduzir a necessidade de revisão, ajuda na interação entre os participantes.

## 3. Abordagem de Engenharia de Requisitos

Para a abordagem de Engenharia de Requisitos também utilizamos como base o Cascata. O modelo possui todas as atividades presentes na engenharia de requisitos, seguindo uma linearidade quanto a ordem de execução das etapas. 

Segue imagem com os processos abaixo:

<p align="center">
  <img src="https://github.com/FGAUnB-REQ-GM/2021.2-DepBot/blob/doc_visao/docs/assets/cascataProcessos.png?raw=true">
</p>

### 3.1 Elicitação de Requisitos

|Atividade|Método|Ferramenta|
|:--------|:-----|:---------|
|Identificação de requisitos funcionais|Cenários|Software de edição de texto|
|Identificação de requisitos não funcionais|Cenários|Software de edição de texto|

### 3.2 Análise de Requisitos

|Atividade|Método|Ferramenta|
|:--------|:-----|:---------|
|Classificação de requisitos|Brainstorming|Serviço de comunicação remota|
|Definição das prioridades|Brainstorming|Serviço de comunicação remota|
|Resolução de conflitos|Brainstorming|Serviço de comunicação remota|

### 3.3 Documentação de Requisitos
|Atividade|Método|Ferramenta|
|:--------|:-----|:---------|
|Documentar requisitos de usuário|Linguagem natural|Software de edição de texto|
|Documentar requisitos de sistema|Linguagem natural|Software de edição de texto|
|Registrar os requisitos aprovados de forma clara|Linguagem natural|Software de edição de texto|
|Documentar possíveis alterações nos requisitos|Linguagem natural|Software de edição de texto|

### 3.4 Verificação de Requisitos

|Atividade|Método|Ferramenta|
|:--------|:-----|:---------|
|Realismo|Revisões de requisitos|Software de edição de texto|
|Completude|Revisões de requisitos|Software de edição de texto|
|Consistência|Revisões de requisitos|Software de edição de texto|
|Validação|Revisões de requisitos|Software de edição de texto|
|Verificabilidade|Geração de casos de teste|Telegram|

### 3.5 Gerenciamento de Requisitos

|Atividade|Método|Ferramenta|
|:--------|:-----|:---------|
|Identificação dos Requisitos|Decidir um padrão de nomenclatura e aplicar sequencialmente sobre os requisitos|Google Sheets|
|Armazenamento dos Requisitos|Armazenar a identificação e suas respectivas informações|Google Sheets|
|Rastreabilidade dos Requisitos|Matriz de Rastreabilidade|Google Sheets|

## 4. Visão Geral do Projeto

### 4.1 Organização do Projeto 

A organização do projeto irá levar em conta a abordagem de desenvolvimento de software escolhida, o Cascata. Nela utilizaremos uma estrutura tradicional de uma equipe de desenvolvimento de software, entretanto, algumas adaptações serão realizadas no modelo para uma melhor adequação no projeto. Levando em conta que no modelo cascata a fase de testes ocorre somente nos estágios finais e que desejamos a participação de todos na codificação, duas foram as modificações na organização: 

- O gerente do projeto irá assumir também o papel de desenvolvedor caso suas atribuições semanais já tenham sido finalizadas.
- O testador também irá acompanhar e participar do desenvolvimento caso suas atribuições semanais já tenham sido finalizadas.

Segue tabela com os papéis da equipe:

|Papel|Atribuições|Responsáveis|Participantes|
|:--------|:-----|:---------|:---------|
|Gerente do projeto|Acompanhar e gerenciar a equipe; Garantir um bom andamento do projeto; Preparar atas para as reuniões; Criação e fechamento de issues; Participar com papel secundário no desenvolvimento; Documentos de abertura e fechamento de Sprints; Trabalhar na documentação.|Pedro Lucas||
|Desenvolvedor|Codificação do software; Definir e seguir um padrão para organização dos códigos; Analisar e implementar possíveis melhorias na aplicação; Trabalhar na documentação.|Pedro Vieira e Victor Cabral| Vinícius Roriz, Lucas Braun e Pedro Lucas|
|Testador|Executar testes no software; Resolução de bugs; Definir e preparar ambiente de desenvolvimento; Participar com papel secundário no desenvolvimento; Trabalhar na documentação.|Vinícius Roriz e Lucas Braun|Pedro Vieira e Victor Cabral|
### 4.2 Planejamento das Fases e/ou Iterações do Projeto

|Sprint|Produto(Entrega)|Data Início|Data Fim|
|:--------|:-----|:---------|:---------|
|||||
### 4.3	Matriz de Comunicação

|Descrição|Área/Envolvidos|Periodicidade|Produtos Gerados|
|:--------|:-----|:---------|:---------|
|Acompanhamento das Atividades em Andamento|Equipe do Projeto|Semanal|Ata de reunião|
|Acompanhamento dos Riscos, Compromissos, Ações Pendentes, Indicadores|Equipe do Projeto|Quinzenal|Relatório de situação do projeto|
|Comunicar situação do projeto|Equipe do Projeto e Professor|Semanal|Relatório de situação do projeto|

### 4.4	Gerenciamento de Riscos

Para o Gerenciamento de Riscos devem ser realizadas tarefas, como:  

-	Identificar todos os riscos possíveis e detectáveis em cada fase do projeto;
-	Executar as ações para mitigar os riscos que tenham um alto grau de exposição ao risco caso este ocorra na Lista de Riscos do Projeto;
-	Fazer uma revisão da lista dos riscos periodicamente, com o propósito de averiguar uma possível incidência de um risco e ver se há outros riscos ainda não relatados;
-	Em caso de confirmação de um risco previsto, agir no sentido de contingenciá-lo conforme programado;
-	Registrar os riscos no Painel de Controle do Projeto e no Plano do Projeto (Riscos iniciais);

### 4.5	Critérios de Replanejamento

Replanejamento mediante:
- Orientação do monitor ou professor responsável pela turma;
- Consenso entre o grupo;

## 5. Lições Aprendidas

### 5.1 Unidade 1

Na Unidade 1 foi possível aprender sobre os fundamentos, abordagens e diferentes processos da Engenharia de Requisitos. Fomos também introduzidos as atividades de elicitação, análise, documentação, verificação e gerenciamento de requisitos e a alguns dos métodos que podem ser usados para concluí-las.

Também revisamos as metodologias ágeis e exploramos mais o Cascata, que acabou sendo escolhido para o projeto da disciplina. Ainda sobre as metodologias, aprendemos que se pode utilizar princípios de práticas ágeis mesmo quando a estrutura principal utilizada é sequencial.

### 5.2 Unidade 2

## 6. Referências Bibliográficas

SOMMERVILLE, Ian. Engenharia de Software. 10ª ed., Pearson, 2018.

Kotonya, G. and Sommerville, I. (1998) Requirements Engineering: Processes and Techniques. John Wiley & Sons, Chichester.
