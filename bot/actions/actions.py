# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset, SlotSet, ConversationPaused, Restarted
import requests


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world2"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        nome = tracker.get_slot("name")
        sobrenome = tracker.get_slot("sobrenome")
        id_deputado = tracker.get_slot("idDep")
        nome_p = nome + " " + sobrenome

        texto_erro = "Infelizmente não consegui encontrar o deputado, tente digitar outro nome =)"
        request = requests.get(
            'https://dadosabertos.camara.leg.br/api/v2/deputados?nome=%s&ordem=ASC&ordenarPor=nome' % nome_p).json()
        if(len(request["dados"]) == 0):
            dispatcher.utter_message(text=texto_erro)
            return [Restarted()]
        else:

            id_deputado = request["dados"][0]["id"]
            SlotSet("idDep", id_deputado)

        return [SlotSet("idDep", id_deputado)]


class ActionSetIdPartido(Action):

    def name(self) -> Text:
        return "action_setIdDeputado"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        nome_partido = tracker.get_slot("partidoPolitico")
        id_partido = tracker.get_slot("idPartidoPolitico")

        request = requests.get(
            'https://dadosabertos.camara.leg.br/api/v2/partidos?sigla=%s&ordem=ASC&ordenarPor=sigla' % nome_partido).json()
        if(len(request["dados"]) == 0):
            texto_erro = "Infelizmente não consegui encontrar o partido, tente digitar outro nome =)"
            dispatcher.utter_message(text=texto_erro)
            return [Restarted()]
        else:
            id_partido = request["dados"][0]["id"]

            SlotSet("idPartidoPolitico", id_partido)

        return [SlotSet("idPartidoPolitico", id_partido)]


class MostraDados(Action):
    def name(self) -> Text:
        return "action_mostraDados"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        id_deputado = tracker.get_slot("idDep")
        if(id_deputado != None):
            id_deputado_str = str(id_deputado)

            request = requests.get(
                'https://dadosabertos.camara.leg.br/api/v2/deputados/%s' % id_deputado_str).json()
            email = request["dados"]["ultimoStatus"]["email"]
            texto = "O email é " + email + "!"
            dispatcher.utter_message(text=texto)
            return [SlotSet("name", None), SlotSet("sobrenome", None)]
        else:
            texto_erro = "Infelizmente não encontrei os dados =( . Por favor tente começar novamente digitando outro nome de deputado."
            dispatcher.utter_message(text=texto_erro)
            return [Restarted()]
        return []


class MostraReumoDeputado(Action):
    def name(self) -> Text:
        return "action_mostra_resumo"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        id_deputado = tracker.get_slot("idDep")
        if(id_deputado is not None):
            id_deputado_str = str(id_deputado)
            request = requests.get('https://dadosabertos.camara.leg.br/api/v2/deputados/%s'%id_deputado_str).json()
            request2 = requests.get('https://dadosabertos.camara.leg.br/api/v2/deputados/%s/profissoes'%id_deputado_str).json()

            nome_civil = 'Desconhecido'
            nome_eleitoral = 'Desconhecido'
            email = 'Desconhecido'
            partido = 'Desconhecido'
            sexo_t = ''
            esolaridade = 'Desconhecido'
            municipio_nascimento = 'Desconhecido'
            profissao = 'Desconhecido'
            foto = 'Desconhecido'

            if request["dados"]["nomeCivil"] is not None:
                nome_civil = request["dados"]["nomeCivil"]

            if request["dados"]["ultimoStatus"]["nomeEleitoral"] is not None:
                nome_eleitoral = request["dados"]["ultimoStatus"]["nomeEleitoral"]

            if request["dados"]["sexo"] is not None:
                sexo = request["dados"]["sexo"]
                if(sexo == 'F'):
                    sexo_t = 'Feminino'
                else:
                    sexo_t = 'Masculino'

            if request["dados"]["ultimoStatus"]["siglaPartido"] is not None:
                partido = request["dados"]["ultimoStatus"]["siglaPartido"]

            if request["dados"]["ultimoStatus"]["email"] is not None:
                email = request["dados"]["ultimoStatus"]["email"]

            if request["dados"]["escolaridade"] is not None:
                esolaridade = request["dados"]["escolaridade"]

            if request["dados"]["ufNascimento"] is not None:
                uf_nascimento = request["dados"]["ufNascimento"]

            if request["dados"]["municipioNascimento"] is not None:
                municipio_nascimento = request["dados"]["municipioNascimento"]

            if request2["dados"][0]["titulo"] is not None:
                profissao = request2["dados"][0]["titulo"]

            if request["dados"]["ultimoStatus"]["urlFoto"] is not None:
                foto = request["dados"]["ultimoStatus"]["urlFoto"]

            texto1 = 'Segue abaixo os dados que consegui sobre ' + nome_civil
            texto2 = '- Nome Civil: ' + nome_civil + '\n' + '- Nome Eleitoral: ' + nome_eleitoral + '\n' + '- Email: ' + email + '\n' + '- Partido: ' + partido + '\n' + \
                '- Sexo: ' + sexo_t + '\n' + '- Escolaridade: ' + esolaridade + '\n' + '- UF Nascimento: ' + \
                uf_nascimento + '\n' + '- Município Nascimento: ' + \
                municipio_nascimento + '\n' + '- Profissões: ' + profissao
            texto3 = foto
            dispatcher.utter_message(text=texto1)
            dispatcher.utter_message(text=texto2)
            dispatcher.utter_message(text=texto3)
            return [SlotSet("name", None), SlotSet("sobrenome", None)]
        else:
            texto_erro = "Infelizmente não encontrei os dados 😔 . Por favor tente começar novamente digitando outro nome de deputado."
            dispatcher.utter_message(text=texto_erro)
            return [Restarted()]
        return []


class MostraResumoPartido(Action):
    def name(self) -> Text:
        return "action_mostra_resumo_partido"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        id_partido = tracker.get_slot("idPartidoPolitico")
        if(id_partido is not None):
            id_partido_str = str(id_partido)
            nome_partido = 'Desconhecido'
            sigla_partido = 'Desconhecido'
            situacao_partido = 'Desconhecido'
            total_membros_partido = 'Desconhecido'

            request = requests.get(
                'https://dadosabertos.camara.leg.br/api/v2/partidos/%s' % id_partido_str).json()

            if request["dados"]["nome"] is not None:
                nome_partido = request["dados"]["nome"]
            if request["dados"]["sigla"] is not None:
                sigla_partido = request["dados"]["sigla"]
            if request["dados"]["status"]["situacao"] is not None:
                situacao_partido = request["dados"]["status"]["situacao"]
            if request["dados"]["status"]["totalMembros"] is not None:
                total_membros_partido = request["dados"]["status"]["totalMembros"]

            texto1 = "Segue abaixo o resumo dos dados do partido..."
            texto2 = "- Nome: " + nome_partido + "\n" + "- Sigla: " + sigla_partido + "\n" + \
                "- Situação: " + situacao_partido + "\n" + \
                "- Número de membros: " + total_membros_partido
            dispatcher.utter_message(text=texto1)
            dispatcher.utter_message(text=texto2)

            return [SlotSet("partidoPolitico", None)]

        else:
            texto_erro = "Infelizmente não encontrei os dados 😔 . Por favor tente começar novamente digitando outra sigla de partido."
            dispatcher.utter_message(text=texto_erro)
            return [Restarted()]
        return []


class MostraSituacao(Action):
    def name(self) -> Text:
        return "action_mostraSituacao"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        id_deputado = tracker.get_slot("idDep")
        id_deputado_str = str(id_deputado)
        request = requests.get(
            'https://dadosabertos.camara.leg.br/api/v2/deputados/%s' % id_deputado_str).json()
        situacao = request["dados"]["ultimoStatus"]["situacao"]
        exer = "Exercício"
        texto = ""
        if situacao == exer:
            texto = "O Deputado está em exercício."
        else:
            texto = "O Deputado não está mais em exercício."
        dispatcher.utter_message(text=texto)
        return []


class MostraListaPartidos(Action):
    def name(self) -> Text:
        return "action_mostraListaPartidos"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        request = requests.get(
            'https://dadosabertos.camara.leg.br/api/v2/partidos?itens=50&ordem=ASC&ordenarPor=sigla').json()
        lista = request["dados"]
        lista_array = []
        for item in lista:
            lista_array.append(item["sigla"] + "\n")
        texto2 = "".join(lista_array)
        texto = "Alguns dos partidos políticos disponíveis são..."

        dispatcher.utter_message(text=texto)
        dispatcher.utter_message(text=texto2)

        return []


class MostraListaPartidos(Action):
    def name(self) -> Text:
        return "action_mostraListaPartidos"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        request = requests.get(
            'https://dadosabertos.camara.leg.br/api/v2/partidos?itens=50&ordem=ASC&ordenarPor=sigla').json()
        lista = request["dados"]
        lista_array = []
        for item in lista:
            lista_array.append(item["sigla"] + "\n")
        texto2 = "".join(lista_array)
        texto = "Alguns dos partidos políticos disponíveis são..."

        dispatcher.utter_message(text=texto)
        dispatcher.utter_message(text=texto2)

        return []


class MostraMembrosPartido(Action):
    def name(self) -> Text:
        return "action_mostraMembrosPartido"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        id_partido = tracker.get_slot("idPartidoPolitico")
        if(id_partido != None):
            id_partido_str = str(idPartido)
            request = requests.get(
                'https://dadosabertos.camara.leg.br/api/v2/partidos/%s' % id_partido_str).json()
            membros = request["dados"]["status"]["totalMembros"]
            print(idPartido)
            texto = "O partido conta com um total de " + membros + " membros !!"
            dispatcher.utter_message(text=texto)
            return [SlotSet("partidoPolitico", None)]

        else:
            texto_erro = "Infelizmente não encontrei os dados =( . Por favor tente começar novamente digitando outro nome de deputado."
            dispatcher.utter_message(text=texto_erro)
            return [Restarted()]
        return []


class MostraListaDeputadosPorPartido(Action):
    def name(self) -> Text:
        return "action_MostraListaDeputadosPorPartido"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        sigla = tracker.get_slot("partidoPolitico")
        request = requests.get(
            'https://dadosabertos.camara.leg.br/api/v2/deputados?siglaUf=&siglaPartido=%s&itens=50&ordem=ASC&ordenarPor=nome' % sigla).json()
        texto = ""
        texto2 = ""
        if not request["dados"]:
            texto = "Desculpa, não consegui encontrar os deputados desse partido, digite outro ou digite 'Lista Partidos' para ver quais partidos estão disponíveis =)."
            dispatcher.utter_message(text=texto)
            return [SlotSet("partidoPolitico", None)]
        else:
            lista_deputados = request["dados"]
            lista_array_deputados = []

            for item in lista_deputados:
                lista_array_deputados.append(item["nome"] + "\n")

            texto = "Segue abaixo uma lista de deputados disponíveis para a consulta do partido " + sigla
            texto2 = "".join(lista_array_deputados)

            dispatcher.utter_message(text=texto)
            dispatcher.utter_message(text=texto2)

            return [SlotSet("partidoPolitico", None)]

