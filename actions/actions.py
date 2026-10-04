# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from .weather import get_weather
#
#
class ActionWeatherUpdate(Action):

    def name(self) -> Text:
        return "get_weather_update"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        city = tracker.get_slot("city")

        if city:
            main, temp, feels_like = get_weather(city)

            dispatcher.utter_message(
                text="In {city}, there is mainly {main}. "
                     "The temperature currently is {temp}°C "
                     "and it feels like {feels_like}°C."
                .format(
                    city=city,
                    main=main,
                    temp=temp,
                    feels_like=feels_like
                )
            )
        else:
            dispatcher.utter_message(
                text="Please tell me which city you want the weather for."
            )

        return []