import yaml

import discord

from bot.templates import template
from bot.feature_syllabus import get_sessions
from bot.feature_intent_recognition import pizza_intent
from bot.feature_dialogue import CashierDialogueFSM

class CLCL2021Client(discord.Client):

    def __init__(self, **options):
        super().__init__(**options)
        self.cashier_dialogues = {}

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):

        print('Message from {0.author}: {0.content}'.format(message))

        # We don't want to reply/work with our own messages
        if self.user.id != message.author.id:


            '''1. Cashier Dialogue
            Users can 'enter' the store by typing 'Enter Store'. As long as the dialogue has not finished, we will stay
            in the store dialogue for this particular user.
            '''
            if message.author.name in self.cashier_dialogues.keys():
                dialogue = self.cashier_dialogues[message.author.name]

                if not dialogue.finished:
                    await message.channel.send(f'[STORE {message.author.name}]: {dialogue.handle_message(message.content)}')
                    return True
    
            if message.content.startswith('Enter Store'):
                self.cashier_dialogues[message.author.name] = CashierDialogueFSM(message.author.name)
                await message.channel.send(f'[STORE {message.author.name}]: Welcome to the store!')
                return True
        
            '''2. A very basic reply. If the bot sees 'Hi' it will respond 'Hello' on the same channel.
            greet intent; strictly rule based'''
            if message.content.startswith('Hi'):
                await message.channel.send(template('greet', message.author.name))

            '''3. This will trigger if one the keywords is in the message.
            syllabus intent; strictly rule based'''
            session_triggers = ['session', 'class']

            if bool([_ for _ in session_triggers if (_ in message.content)]):

                previous_session, next_session = get_sessions()
                await message.channel.send(f'The last session on *{previous_session["title"]}* was on {previous_session["date"]}.')
                await message.channel.send(f'The next session on *{next_session["title"]}* will be on **{next_session["date"]}**.')

            '''4. Intent Recognition - Pizza
            If we had multiple intent systems, we would need to find a better way of going trough all of them'''
            intent = pizza_intent(message.content)

            if intent == 'pizza_menu':
                await message.channel.send(template('pizza_menu'))
            if intent == 'pizza_order':
                await message.channel.send(template('pizza_order'))
            if intent == 'coke_order':
                await message.channel.send(template('coke_order'))