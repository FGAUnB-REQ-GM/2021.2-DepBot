# Visão do Produto e Projeto

## Histórico de Versões
|Data|Versão|Modificação|Autores|
|:---|:-----|:----------|:------|
|29/01/2022|0.1|Criação do documento|Lucas Braun, Pedro Lucas, Pedro Vieira, Victor Cabral, Vinicius Roriz|
|31/01/2022|0.2|Adição de novas informações nos tópicos do documento|Lucas Braun, Pedro Lucas, Pedro Vieira, Victor Cabral, Vinicius Roriz|
|02/02/2022|0.3|Revisão e melhoria nos textos|Lucas Braun, Pedro Lucas, Pedro Vieira, Victor Cabral, Vinicius Roriz|
|08/02/2022|0.4|Implementação do feedback na seção 2|
## 1. Visão Geral do Produto

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
|**Que**|Disponibiliza informações de deputados aos usuários.|
|**Ao contrário**|De pesquisar individualmente as informações de cada candidato.|
|**Nosso produto**|Proporciona as informações diretamente no Telegram. |

### 1.3 Objetivos do Produto

O objetivo do produto é fornecer informações sobre os deputados brasileiros à população eleitoral para que a mesma tenha conhecimento sobre o que o candidato a deputado e sua frente parlamentar são, prometem fazer e/ou já fizeram em seu mandato. Com o DepBot, o usuário poderá receber informações como discursos, despesas, frente parlamentar, eventos, ocupações, órgãos, etc. do candidato que ele pesquisar sobre. Assim, conhecendo mais sobre o deputado.
	
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
|Especificação de Requisitos de Software (Software Requirements Specification ou SRS)|Linguagem natural e Notação gráfica|Software de edição de texto e editor gráfico Figma|
|Requisitos de Usuário (presente no SRS)|Linguagem natural e Notação gráfica|Software de edição de texto e editor gráfico Figma|
|Requisitos de Sistema (presente no SRS)|Linguagem natural e Notação gráfica|Software de edição de texto e editor gráfico Figma|

### 3.4 Verificação de Requisitos

|Atividade|Método|Ferramenta|
|:--------|:-----|:---------|
Planejamento|Brainstorming|Serviço de Comunicação Remota e Software de edição de texto|
Apresentação|Apresentação em Grupo por Chamada|Serviço de Comunicação Remota|
Preparação|Encontro por Chamada de Vídeo|Serviço de Comunicação Remota|
Reunião de Inspeção|Reunião por Chamada de Vídeo|Serviço de Comunicação Remota|
Correção|Observar, Documentar e Consertar|Software de edição de texto|
Acompanhamento|Brainstorming, Reunião|Serviço de Comunicação Remota|

### 3.5 Gerenciamento de Requisitos

|Atividade|Método|Ferramenta|
|:--------|:-----|:---------|
|Identificação dos Requisitos|Decidir um padrão de nomenclatura e aplicar sequencialmente sobre os requisitos|Software de edição de texto|
|Armazenamento dos Requisitos|Armazenar a identificação e suas respectivas informações|Plataforma GitHub|
|Rastreabilidade dos Requisitos|Matriz de Rastreabilidade|Software de edição de texto|

## 4. Lições Aprendidas

### 4.1 Unidade 1

Na Unidade 1 foi possível aprender sobre os fundamentos, abordagens e diferentes processos da Engenharia de Requisitos. Fomos também introduzidos as várias atividades da engenharia de requisitos e a alguns dos métodos que podem ser usados para concluí-las.

## Referências Bibliográficas

SOMMERVILLE, Ian. Engenharia de Software. 10ª ed., Pearson, 2018.

Kotonya, G. and Sommerville, I. (1998) Requirements Engineering: Processes and Techniques. John Wiley & Sons, Chichester.
