# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset , SlotSet , ConversationPaused , Restarted
import requests

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world2"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        nome = tracker.get_slot("name")
        sobrenome = tracker.get_slot("sobrenome")
        idDeputado = tracker.get_slot("idDep")
        nomeP = nome + " "+ sobrenome
        #print(nomeP)
        textoErro = "Infelizmente não consegui encontrar o deputado, tente digitar outro nome =)"
        request = requests.get('https://dadosabertos.camara.leg.br/api/v2/deputados?nome=%s&ordem=ASC&ordenarPor=nome'%nomeP).json()
        if(len(request["dados"]) == 0):
            dispatcher.utter_message(text=textoErro)
            return [Restarted()]
        else:

            idDeputado = request["dados"][0]["id"]
            SlotSet("idDep" , idDeputado)
    
        return [SlotSet("idDep" , idDeputado)] #,  SlotSet("name", None) , SlotSet("sobrenome" , None)]


class ActionSetIdPartido(Action):

    def name(self) -> Text:
        return "action_setIdDeputado"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        nomePartido = tracker.get_slot("partidoPolitico")
        idPartido = tracker.get_slot("idPartidoPolitico")
    
        request = requests.get('https://dadosabertos.camara.leg.br/api/v2/partidos?sigla=%s&ordem=ASC&ordenarPor=sigla'%nomePartido).json()
        if(len(request["dados"]) == 0):
            textoErro = "Infelizmente não consegui encontrar o partido, tente digitar outro nome =)"
            dispatcher.utter_message(text=textoErro)
            return [Restarted()]
        else:
            idPartido = request["dados"][0]["id"]

            SlotSet("idPartidoPolitico" , idPartido)

       # dispatcher.utter_message(text="Hello World!123")
        #print(type(nomeP))
        return [SlotSet("idPartidoPolitico", idPartido)] #,  SlotSet("partidoPolitico", None)]


class MostraDados(Action):
    def name(self) -> Text:
        return "action_mostraDados"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        idDeputado = tracker.get_slot("idDep")
        if(idDeputado != None):
            idDeputadoStr = str(idDeputado)
    
            request = requests.get('https://dadosabertos.camara.leg.br/api/v2/deputados/%s'%idDeputadoStr).json()
            email = request["dados"]["ultimoStatus"]["email"]
            texto = "O email é " + email + "!"
            dispatcher.utter_message(text=texto)
            return [SlotSet("name", None) , SlotSet("sobrenome" , None)]
        else:
            textoErro = "Infelizmente não encontrei os dados =( . Por favor tente começar novamente digitando outro nome de deputado."
            dispatcher.utter_message(text=textoErro)
            return [Restarted()]
        return []

class MostraReumoDeputado(Action):
    def name(self) -> Text:
        return "action_mostra_resumo"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        idDeputado = tracker.get_slot("idDep")
        if(idDeputado is not None):
            idDeputadoStr = str(idDeputado)
            request = requests.get('https://dadosabertos.camara.leg.br/api/v2/deputados/%s'%idDeputadoStr).json()
            nomeCivil = 'Desconhecido'
            nomeEleitoral = 'Desconhecido'
            email = 'Desconhecido'
            partido = 'Desconhecido'
            sexoT = ''
            esolaridade = 'Desconhecido'
            municipioNascimento = 'Desconhecido'

            if request["dados"]["nomeCivil"] is not None:
                nomeCivil = request["dados"]["nomeCivil"]
            
            if request["dados"]["ultimoStatus"]["nomeEleitoral"] is not None:
                nomeEleitoral = request["dados"]["ultimoStatus"]["nomeEleitoral"]

            if request["dados"]["sexo"] is not None:
                sexo = request["dados"]["sexo"]
                if(sexo == 'F'):
                    sexoT = 'Feminino'
                else:
                    sexoT = 'Masculino'


            if request["dados"]["ultimoStatus"]["siglaPartido"] is not None:
                partido = request["dados"]["ultimoStatus"]["siglaPartido"]

            if request["dados"]["ultimoStatus"]["email"] is not None:
                #email = 'Teste'
                email = request["dados"]["ultimoStatus"]["email"]
            
            if request["dados"]["escolaridade"] is not None:
                esolaridade = request["dados"]["escolaridade"]

            if request["dados"]["ufNascimento"] is not None:
                ufNascimento = request["dados"]["ufNascimento"]

            if request["dados"]["municipioNascimento"] is not None:
                municipioNascimento = request["dados"]["municipioNascimento"]
            
            texto1 = 'Segue abaixo os dados que consegui sobre ' + nomeCivil
            texto2 = '- Nome Civil: ' + nomeCivil + '\n' + '- Nome Eleitoral: ' + nomeEleitoral + '\n' + '- Email: ' + email + '\n'+ '- Partido: ' + partido + '\n' + '- Sexo: ' + sexoT + '\n' + '- Escolaridade: ' + esolaridade + '\n' +  '- UF Nascimento: ' + ufNascimento + '\n' + '- Município Nascimento: ' + municipioNascimento
            dispatcher.utter_message(text=texto1)
            dispatcher.utter_message(text=texto2)
            return [SlotSet("name", None) , SlotSet("sobrenome" , None)]
        else:
            textoErro = "Infelizmente não encontrei os dados 😔 . Por favor tente começar novamente digitando outro nome de deputado."
            dispatcher.utter_message(text=textoErro)
            return [Restarted()]
        return []


class MostraResumoPartido(Action):
    def name(self) -> Text:
        return "action_mostra_resumo_partido"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        idPartido = tracker.get_slot("idPartidoPolitico")
        if(idPartido is not None):
            idPartidoStr = str(idPartido)

            request = requests.get('https://dadosabertos.camara.leg.br/api/v2/partidos/%s'%idPartidoStr).json()
            nomePartido = request["dados"]["nome"] 
            siglaPartido = request["dados"]["sigla"]
            situacaoPartido = request["dados"]["status"]["situacao"]
            totalMembrosPartido = request["dados"]["status"]["totalMembros"]
            #nomeLider = request["dados"]["status"]["lider"]["nome"]
            #imagemPartido = request["dados"]["urlLogo"]

            texto1 = "Segue abaixo o resumo dos dados do partido..."
            texto2 = "- Nome: " + nomePartido + "\n" + "- Sigla: " + siglaPartido + "\n" + "- Situação: " + situacaoPartido + "\n" + "- Número de membros: " + totalMembrosPartido
            dispatcher.utter_message(text=texto1)
            dispatcher.utter_message(text=texto2)

            return [SlotSet("partidoPolitico", None)]

        else:
            textoErro = "Infelizmente não encontrei os dados 😔 . Por favor tente começar novamente digitando outra sigla de partido."
            dispatcher.utter_message(text=textoErro)
            return [Restarted()]
        return []



class MostraSituacao(Action):
    def name(self) -> Text:
        return "action_mostraSituacao"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        idDeputado = tracker.get_slot("idDep")
        idDeputadoStr = str(idDeputado)
        request = requests.get('https://dadosabertos.camara.leg.br/api/v2/deputados/%s'%idDeputadoStr).json()
        situacao = request["dados"]["ultimoStatus"]["situacao"]
        exer = "Exercício"
        texto = ""
        if situacao == exer:
            texto = "O Deputado está em exercício."
        else:
            texto = "O Deputado não está mais em exercício."
        dispatcher.utter_message(text=texto)
        #print('https://dadosabertos.camara.leg.br/api/v2/deputados/$s'%idDeputadoStr)
        print(type(situacao))
        print(texto)
        return []

class MostraListaPartidos(Action):
    def name(self) -> Text:
        return "action_mostraListaPartidos"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        request = requests.get('https://dadosabertos.camara.leg.br/api/v2/partidos?itens=50&ordem=ASC&ordenarPor=sigla').json()
        lista = request["dados"]
        listaArray = []
        for item in lista:
            listaArray.append(item["sigla"] + "\n")
        texto2 = "".join(listaArray)
        texto = "Alguns dos partidos políticos disponíveis são..."
        print(texto2)
        dispatcher.utter_message(text=texto)
        dispatcher.utter_message(text=texto2)

        return []

class MostraListaPartidos(Action):
    def name(self) -> Text:
        return "action_mostraListaPartidos"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        request = requests.get('https://dadosabertos.camara.leg.br/api/v2/partidos?itens=50&ordem=ASC&ordenarPor=sigla').json()
        lista = request["dados"]
        listaArray = []
        for item in lista:
            listaArray.append(item["sigla"] + "\n")
        texto2 = "".join(listaArray)
        texto = "Alguns dos partidos políticos disponíveis são..."
        print(texto2)
        dispatcher.utter_message(text=texto)
        dispatcher.utter_message(text=texto2)

        return []

class MostraMembrosPartido(Action):
    def name(self) -> Text:
        return "action_mostraMembrosPartido"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        idPartido = tracker.get_slot("idPartidoPolitico")
        if(idPartido != None):
            idPartidoStr = str(idPartido)
            request = requests.get('https://dadosabertos.camara.leg.br/api/v2/partidos/%s'%idPartidoStr).json()
            membros = request["dados"]["status"]["totalMembros"]
            print(idPartido)
            texto = "O partido conta com um total de " + membros + " membros !!"
            dispatcher.utter_message(text=texto)
            return [SlotSet("partidoPolitico", None)]

        else:
            textoErro = "Infelizmente não encontrei os dados =( . Por favor tente começar novamente digitando outro nome de deputado."
            dispatcher.utter_message(text=textoErro)
            return [Restarted()]
        return []
