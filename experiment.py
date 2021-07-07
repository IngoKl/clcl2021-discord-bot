from bot.templates import template
from bot.feature_syllabus import get_sessions
from bot.feature_intent_recognition import pizza_intent
from bot.feature_dialogue import CashierDialogueFSM

response = pizza_intent('I want a slice')

print(response)