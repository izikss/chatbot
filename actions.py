"""from rasa_core.actions import Action
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

class ActionCheckRestaurants(Action):
   def name(self):
      # type: () -> Text
      return "action_check_restaurants"

   def run(self, dispatcher, tracker, domain):
      # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]

      cuisine = tracker.get_slot('cuisine')
      q = "select * from restaurants where cuisine='{0}' limit 1".format(cuisine)
      result = db.query(q)

      return [SlotSet("matches", result if result is not None else [])]
   """


from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet


class Form(Action):
    def name(self):
        return 'print_form'

    def run(self, dispatcher, tracker, domain):

        response = "formulaire_Client_Derangement.html"
        dispatcher.utter_message(response)


        return 0