from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import FollowupAction

from rasa_sdk.events import SlotSet

import datetime as dt


class ActionAskDestination(Action):
    def name(self) -> Text:
        return "action_ask_destination"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        destination = tracker.get_slot("destination")

        if not destination:
            dispatcher.utter_message(
                text="I'm sorry, I didn't catch your destination. Can you please tell me your destination city?"
            )
            return [FollowupAction("action_listen")]  # Listen for the next user message

        return [SlotSet("destination", destination)]




    

class ActionCheckGate(Action):
    def name(self) -> Text:
        return "action_check_gate"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        destination = tracker.get_slot("destination")

        if destination.lower() == "us":
            dispatcher.utter_message(text="All the flights to US depart from gate Number 2")
        elif destination.lower() == "canada":
            dispatcher.utter_message(text="All the flights to Canada depart from gate Number 7")
        else:
            dispatcher.utter_message(text="Sorry, we don't have flights to that destination.")

        return []
    
class ActionChecktakeoftime(Action):
    def name(self) -> Text:
        return "action_check_take_of_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        destination = tracker.get_slot("destination")

        if destination.lower() == "us":
            dispatcher.utter_message(text="Every day our flight to the US take off at 9:00 am")
        elif destination.lower() == "canada":
            dispatcher.utter_message(text="Every day our flight to Canada take off at 4:00 pm")
        else:
            dispatcher.utter_message(text="Sorry, we don't have flights to that destination.")

        return []


class ActionCheckLandingtime(Action):
    def name(self) -> Text:
        return "action_check_Landing_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        destination = tracker.get_slot("destination")

        if destination.lower() == "us":
            dispatcher.utter_message(text="Every day our flight to the US land in Halifax Stanfield International Airport at 06:00 pm (in local time")
        elif destination.lower() == "canada":
            dispatcher.utter_message(text="Every day our flight to Canada land in New York International Airport at 11:00 am (in local time")
        else:
            dispatcher.utter_message(text="Sorry, we don't have flights to that destination.")

        return []

class ActionCheckTraveltime(Action):
    def name(self) -> Text:
        return "action_check_travel_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        destination = tracker.get_slot("destination")

        if destination.lower() == "us":
            dispatcher.utter_message(text="Travel time from London to New York International Airport is 3 hours")
        elif destination.lower() == "canada":
            dispatcher.utter_message(text="Travel time from London to Halifax Stanfield International Airport is 3 hours")
        else:
            dispatcher.utter_message(text="Sorry, we don't have flights to that destination.")

        return []
    
class ActionShowBookingInfo(Action):
    def name(self) -> Text:
        return "action_seat"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        flight_class = tracker.get_slot("class")
        num_seats = tracker.get_slot("number")

        if flight_class and num_seats:
            dispatcher.utter_message(
                text=f"You have booked {num_seats} seat(s) in {flight_class} class."
            )
        else:
            dispatcher.utter_message(
                text="I'm sorry, I couldn't find your booking information. Could you please provide it again?"
            )

        return []

class ActionCheckIn(Action):
    def name(self) -> Text:
        return "action_check_in"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        destination = tracker.get_slot("destination")

        if destination.lower() == "us":
            dispatcher.utter_message(text="You have been checked in for your flight to the US.")
        elif destination.lower() == "canada":
            dispatcher.utter_message(text="You have been checked in for your flight to Canada.")
        else:
            dispatcher.utter_message(text="Sorry, we don't have flights to that destination.")

        return []    
    
class ActionAskPassportNumber(Action):
    def name(self):
        return "action_ask_passport_number"

    def run(self, dispatcher, tracker, domain):
        # You can customize the message as per your requirement
        dispatcher.utter_message(text="Could you please provide your passport number?")
        return []

class ActionAskReferenceNumber(Action):
    def name(self):
        return "action_ask_reference_number"

    def run(self, dispatcher, tracker, domain):
        # You can customize the message as per your requirement
        dispatcher.utter_message(text="Could you please provide your reference number?")
        return []