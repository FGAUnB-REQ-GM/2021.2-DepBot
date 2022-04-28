| DEPBOT                                                        |                  |
| ------------------------------------------------------------- | ---------------- |
| Especificação de Caso de Uso: Consulta de Deputado Específico | Data: 26/04/2022 |

<h1 align="center">Depbot </h1>
<h2 align="center">Caso de Uso: Consulta de Deputado Específico</h2>
<h3>1. Breve Descrição</h3>
<p>&emsp;&emsp;O presente caso de uso descreve o fluxo de atividades englobado pela consulta de um deputado específico, desejado pelo usuário. Um dos principais serviços do Depbot é o da consulta de informações de deputados, na qual o usuário busca pelo deputado por nome e o sistema disponibiliza um resumo das informações do deputado buscado.</p>
<h3>2. Atores</h3>
<p> &emsp; 2.1 Usuário

<p>&emsp;&emsp;&emsp;2.1.1  Repórteres ou empresas de conteúdo que necessitem de dados de deputados para  suas matérias.

&emsp;&emsp;&emsp;2.1.2 Acadêmicos buscando fontes confiáveis para o embasamento em suas pesquisas.

&emsp;&emsp;&emsp;2.1.3 Pessoas sem relação com a área de política, porém com interesse em possuir uma fonte com levantamentos confiáveis a respeito dos deputados.

&emsp;&emsp;&emsp;2.1.4 Funcionários públicos que podem usufruir do sistema para conseguir mais conhecimento sobre os deputados e/ou usá-lo para os guiar em tomadas de decisões.</p></p>

<h3>3. Condições Prévias</h3>
Não se aplica.

<h3>4. Fluxo Básico (FB)</h3>

&emsp;&emsp;4.1 Este caso de uso é iniciado quando o usuário solicitar uma consulta de um deputado específico (FA01)

&emsp;&emsp;4.2 O sistema solicita que o usuário informe o nome do deputado.

&emsp;&emsp;4.3 O usuário informa o primeiro nome do deputado que deseja consultar.

&emsp;&emsp;4.4 O sistema recebe o primeiro nome e guarda.

&emsp;&emsp;4.5 O sistema solicita que o usuário informe o sobrenome do deputado.

&emsp;&emsp;4.6 O usuário informa o sobrenome do deputado.

&emsp;&emsp;4.7 O sistema recebe o nome, busca no banco de dados e disponibiliza as informações do deputado buscado.(RN01)(FE01).

&emsp;&emsp;4.8 O caso de uso é encerrado.

<h3>5. Fluxo Alternativo (FA)</h3>

<p>&emsp;&emsp;5.1 FA01 - Listagem de Deputado

<p>&emsp;&emsp;No passo 4.1 do fluxo básico, o usuário não sabe o nome do deputado então deseja listar os deputados para saber o nome.

&emsp;&emsp;5.1.1 O sistema solicita que o usuário escolha um partido(sigla) para a fazer a listagem.

&emsp;&emsp;5.1.2 O usuário escolhe o partido (RN02)(FE02).

&emsp;&emsp;5.1.3 O sistema lista os deputados segundo partido.

&emsp;&emsp;5.1.4 O caso de uso segue para o passo 4.8 do fluxo básico.</p></p>

<h3>6 Fluxo de Exceção (FE)</h3> 
<p>&emsp;&emsp;6.1 FE01 - Nome inválido</p>
<p>&emsp;&emsp;No passo 4.7 do fluxo básico, caso o nome informado pelo usuário não esteja no banco de dados, o sistema exibe a mensagem: "Infelizmente não consegui encontrar o deputado 😔, digite 'deputado' e tente outro nome válido 😁.". E, o caso de uso  retorna ao passo 4.8 do FB.</p>
<p>&emsp;&emsp;6.1 FE02 - Partido inválido
<p>&emsp;&emsp;No passo 5.1.2 do fluxo alternativo, caso a sigla do partido informado pelo usuário não seja válida, o sistema exibe a mensagem: "Desculpa, não consegui encontrar os deputados desse partido 😔, digite outro ou digite 'Lista Partidos' para ver quais partidos estão disponíveis 😁.". E, o caso de uso  retorna ao passo 4.8 do FB.</p></p>

<h3>7 Regra de Negócio (RN) </h3>

<p>&emsp;&emsp;7.1 RN01 - Validação do Nome
<p>&emsp;&emsp;No passo 4.7 do fluxo básico, para que seja considerado válido o nome do deputado deve estar no banco de dados da API.</p></p>

<p>&emsp;&emsp;7.2 RN02 - Validação do Partido
<p>&emsp;&emsp;No passo 5.1.2 do fluxo alternativo, para que seja considerado válido a sigla, a sigla deve estar no banco de dados.</p></p>

<h3>8. Pós-condições </h3>
<p>Não se aplica</p>
<h3>9. Pontos de Extensão</h3>
<p>Não se aplica. </p>
<hr></hr>

| DEPBOT                                                           |                  |
| ---------------------------------------------------------------- | ---------------- |
| Especificação de Caso de Uso: Consulta de Informações de Partido | Data: 27/04/2022 |

<h1 align="center">Depbot </h1>
<h2 align="center">Caso de Uso: Consulta de Informações de Partido</h2>
<h3>1. Breve Descrição</h3>
<p>&emsp;&emsp;O presente caso de uso descreve o fluxo de atividades englobado pela busca de informações de um partido, especificado pelo usuário. Um dos principais serviços do Depbot é o da consulta de informações de partido, na qual o usuário busca pelo partido e o sistema disponibiliza uma série de informações daquele partido.</p>
<h3>2. Atores</h3>
<p> &emsp; 2.1 Usuário

<p>&emsp;&emsp;&emsp;2.1.1  Repórteres ou empresas de conteúdo que necessitem de dados de deputados para  suas matérias.

&emsp;&emsp;&emsp;2.1.2 Acadêmicos buscando fontes confiáveis para o embasamento em suas pesquisas.

&emsp;&emsp;&emsp;2.1.3 Pessoas sem relação com a área de política, porém com interesse em possuir uma fonte com levantamentos confiáveis a respeito dos deputados.

&emsp;&emsp;&emsp;2.1.4 Funcionários públicos que podem usufruir do sistema para conseguir mais conhecimento sobre os deputados e/ou usá-lo para os guiar em tomadas de decisões.</p></p>

<h3>3. Condições Prévias</h3>
Não se aplica.

<h3>4. Fluxo Básico (FB)</h3>

&emsp;&emsp;4.1 Este caso de uso é iniciado quando o usuário solicitar uma consulta de um partido específico (FA01)

&emsp;&emsp;4.2 O sistema solicita que o usuário informe a sigla do partido.

&emsp;&emsp;4.3 O usuário informa a sigla do partido que deseja consultar (RN01)(FE01).

&emsp;&emsp;4.4 O sistema recebe a sigla, busca no banco de dados e disponibiliza as informações do partido buscado.

&emsp;&emsp;4.5 O caso de uso é encerrado.

<h3>5. Fluxo Alternativo (FA)</h3>

<p>&emsp;&emsp;5.1 FA01 - Listagem de Deputado

<p>&emsp;&emsp;No passo 4.1 do fluxo básico, o usuário não sabe o nome do deputado então deseja listar os deputados para saber o nome.

&emsp;&emsp;5.1.1 O usuário solicita a listagem de partidos.

&emsp;&emsp;5.1.2 O sistema lista os partidos.

&emsp;&emsp;5.1.3 O caso de uso segue para o passo 4.5 do fluxo básico.</p></p>

<h3>6 Fluxo de Exceção (FE)</h3> 
<p>&emsp;&emsp;6.1 FE01 - Partido inválido</p>
<p>&emsp;&emsp;No passo 4.7 do fluxo básico, caso o partido informado pelo usuário não esteja no banco de dados, o sistema exibe a mensagem: “Infelizmente não consegui encontrar o partido 😔, digite 'partido' e tente outra sigla válida 😁.”. E, o caso de uso  retorna ao passo 4.5 do FB.</p>

<h3>7 Regra de Negócio (RN) </h3>

<p>&emsp;&emsp;7.1 RN01 - Validação da Sigla
<p>&emsp;&emsp;No passo 4.3 do fluxo básico, para que seja considerado válido a sigla, a sigla deve estar no banco de dados.</p>
<h3>8. Pós-condições </h3>
<p>Não se aplica</p>
<h3>9. Pontos de Extensão</h3>
<p>Não se aplica. </p>

<hr></hr>

| DEPBOT                                                          |                  |
| --------------------------------------------------------------- | ---------------- |
| Especificação de Caso de Uso: Consulta de Informações da Câmara | Data: 26/04/2022 |

<h1 align="center">Depbot </h1>
<h2 align="center">Caso de Uso: Consulta de Informações da Câmara</h2>
<h3>1. Breve Descrição</h3>
<p>&emsp;&emsp;O presente caso de uso descreve o fluxo de atividades englobado pela consulta de informações da Câmara dos Deputados, desejado pelo usuário. Um dos serviços do Depbot é a consulta de informações gerais sobre a Câmara, na qual o usuário realiza uma pergunta e o sistema disponibiliza a resposta, caso a possua.</p>
<h3>2. Atores</h3>
<p> &emsp; 2.1 Usuário

<p>&emsp;&emsp;&emsp;2.1.1  Repórteres ou empresas de conteúdo que necessitem de dados de deputados para  suas matérias.

&emsp;&emsp;&emsp;2.1.2 Acadêmicos buscando fontes confiáveis para o embasamento em suas pesquisas.

&emsp;&emsp;&emsp;2.1.3 Pessoas sem relação com a área de política, porém com interesse em possuir uma fonte com levantamentos confiáveis a respeito dos deputados.

&emsp;&emsp;&emsp;2.1.4 Funcionários públicos que podem usufruir do sistema para conseguir mais conhecimento sobre os deputados e/ou usá-lo para os guiar em tomadas de decisões.</p></p>

<h3>3. Condições Prévias</h3>
Não se aplica.

<h3>4. Fluxo Básico (FB)</h3>


&emsp;&emsp;4.1 Este caso de uso é iniciado quando o usuário solicitar informações sobre a Câmara dos Deputados

&emsp;&emsp;4.2 O sistema recebe a solicitação e exibe tópicos relacionados para o usuário consultar (RN01).

&emsp;&emsp;4.3 O usuário escolhe um tópico.

&emsp;&emsp;4.4 O sistema exibe informações sobre aquele tópico.

&emsp;&emsp;4.5 O caso de uso é encerrado(RN02)(FE01).

<h3>5. Fluxo Alternativo (FA)</h3>

Não se aplica.

<h3>6 Fluxo de Exceção (FE)</h3> 
<p>&emsp;&emsp;6.1 FE01 - Tópico Alternativo</p>
<p>&emsp;&emsp;No passo 4.5 do fluxo básico, caso o usuário queria consultar outro tópico ele poderá consultar ao digitar o tópico, então o sistema exibe informações sobre o tópico. E, o caso de uso retorna ao passo 4.5 do FB.</p>

<h3>7 Regra de Negócio (RN) </h3>

<p>&emsp;7.1 RN01 - Lista de Tópicos Relacionados</p>
&emsp;No passo 4.2 do fluxo básico, o sistema exibe a seguinte lista de tópicos relaciodos à Câmada dos Deputados:<ul>
<li> História da Câmara dos Deputados</li>
<li> Como funciona a Câmara dos Deputados</li>
<li>Como realizar contato com a Câmara dos Deputados</li></ul>

<p>&emsp;7.2 RN02 - Tópicos Alternativos</p>
&emsp;No passo 4.5 do fluxo básico, o usuário tem a chance de consultar outro tópico.</p>

<h3>8. Pós-condições </h3>
Não se aplica.
<h3>9. Pontos de Extensão</h3>
Não se aplica.

<hr></hr>

| DEPBOT                                                          |                  |
| --------------------------------------------------------------- | ---------------- |
| Especificação de Caso de Uso: Consulta de Informações das Eleições | Data: 26/04/2022 |

<h1 align="center">Depbot </h1>
<h2 align="center">Caso de Uso: Consulta de Informações das Eleições</h2>
<h3>1. Breve Descrição</h3>
<p>&emsp;&emsp;O presente caso de uso descreve o fluxo de atividades englobado pela consulta de informações das eleições, desejado pelo usuário. Um dos serviços do Depbot é a consulta de informações gerais sobre as Eleições, na qual o usuário realiza uma pergunta e o sistema disponibiliza a resposta, caso a possua.</p>
<h3>2. Atores</h3>
<p> &emsp; 2.1 Usuário

<p>&emsp;&emsp;&emsp;2.1.1  Repórteres ou empresas de conteúdo que necessitem de dados de deputados para  suas matérias.

&emsp;&emsp;&emsp;2.1.2 Acadêmicos buscando fontes confiáveis para o embasamento em suas pesquisas.

&emsp;&emsp;&emsp;2.1.3 Pessoas sem relação com a área de política, porém com interesse em possuir uma fonte com levantamentos confiáveis a respeito dos deputados.

&emsp;&emsp;&emsp;2.1.4 Funcionários públicos que podem usufruir do sistema para conseguir mais conhecimento sobre os deputados e/ou usá-lo para os guiar em tomadas de decisões.</p></p>

<h3>3. Condições Prévias</h3>
Não se aplica.

<h3>4. Fluxo Básico (FB)</h3>

&emsp;&emsp;4.1 Este caso de uso é iniciado quando o usuário solicitar informações sobre as Eleições

&emsp;&emsp;4.2 O sistema recebe a solicitação e exibe tópicos relacionados para o usuário consultar (RN01).

&emsp;&emsp;4.3 O usuário escolhe um tópico.

&emsp;&emsp;4.4 O sistema exibe informações sobre aquele tópico.

&emsp;&emsp;4.5 O caso de uso é encerrado(RN02)(FE01).

<h3>5. Fluxo Alternativo (FA)</h3>

Não se aplica.

<h3>6 Fluxo de Exceção (FE)</h3> 
<p>&emsp;&emsp;6.1 FE01 - Escolha de Outro Tópico</p>
<p>&emsp;&emsp;No passo 4.5 do fluxo básico, caso o usuário queria consultar outro tópico ele poderá consultar ao digitar o tópico, então o sistema exibe informações sobre o tópico. E, o caso de uso retorna ao passo 4.5 do FB.</p>

<h3>7 Regra de Negócio (RN) </h3>

<p>&emsp;7.1 RN01 - Lista de Tópicos Relacionados</p>
&emsp;No passo 4.2 do fluxo básico, o sistema exibe a seguinte lista de tópicos relaciodos com as eleições:<ul>
<li> Dia e calendário das eleições</li>
<li> Funcionamento das eleições</li>
<li> Local de votação</li></ul>

<p>&emsp;7.2 RN02 - Tópicos Alternativos</p>
&emsp;No passo 4.5 do fluxo básico, o usuário tem a chance de consultar outro tópico.</p>

<h3>8. Pós-condições </h3>
Não se aplica.
<h3>9. Pontos de Extensão</h3>
Não se aplica.
