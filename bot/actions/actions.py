# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset
import requests

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world2"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #nome = tracker.get_slot("name")
        #request = requests.get('https://dadosabertos.camara.leg.br/api/v2/deputados?nome=%s&ordem=ASC&ordenarPor=nome'%nome).json()
        #print(request["dados"][0]["nome"])
        #print(nome)
        dispatcher.utter_message(text="Hello World!123")

        return []
