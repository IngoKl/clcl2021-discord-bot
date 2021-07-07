# CLCL2021 Discord Bot Template

This is a minimalistic Discord bot template using `discord.py`. This is meant as an exercise starting point for my students taking *Corpus and Computational Linguistics* in 2021.

## Getting Started

1. Follow this [tutorial](https://discordpy.readthedocs.io/en/stable/discord.html) and create a Discord bot user account. You also want to let your bot follow a server. Feel free to use our class server!
2. Create virtual environment for this project and activate it: `python -m venv dicord-bot-env` followed by `source dicord-bot-env/bin/activate`
3. Install the necessary dependencies to your environment: `pip install -r requirements.txt`
4. Copy the `default.yml` file and add your token (see step 1)
5. Run the basic bot using `python bot.py your_config.yml`

## Features

This basic bot includes three demonstrative features:

In `feature_dialogue.py` you will find a dialogue system immitating a cashier/store situation. It is based on a simple state machine. This also demonstrates the idea of an *app* within a more general conversational system.

In `feature_syllabus.py` you will find a simple function that returns the previous and next session in the course. In `bot.py` this is hooked to two keywords that will trigger the function.

In `feature_intent_recognition.py` you will find an example for *Intent Recognition* modeled after Chapter 8 of Yuli Vasiliev's *Natural Language Processing with Python and spaCy*. This is a very basic - possibly also clumsy - implementation. However, it demonstrates what we can do by simply looking at some basic syntactic relations.

## Hints and Notes

You can think of the *dialogue system* (store) as a separate thing. Whenever a user sends a message to the bot, we check whether that user is currently 'in' the store. If that's the case, all messages will be handled by the store dialogue system. Once the user has finished that dialogue, 'regular' bot functions will become available to them again.

The bot supports some basic **templates**. These are strings that the bot will use to reply to a given intent. The `templates.py` handles these templates. Since these templates can also contain entities (e.g., *Hi $entity*), the code looks a little bit more complicated.

The goal of this system is to present the user with a variety of possible answers for a given intent or prompt.

## Caveats

This implementation, while very simple, has one big caveat: For each incoming message, we are going over all of our possible reply options.

This is not very efficient, and it could also cause problems if multiple cases fit the original message. In a real system, you would most likely have some sort of intent recognition at the very beginning before making any further decisions.

The store example hints towards an implementation that some systems use: *apps*. For example, *Amazon's Alexa* offers you the option of using apps. Once you open an app, the whole conversation will be only within the context of that given app. Once you leave the app, your voice commands will be handled by the general system again.

## Outlook

Obviously, this is more or less a toy system. If you are interested, have a look at [*Rasa*](Uhttps://rasa.com/open-source/), a powerful (open source) conversational AI platform with great documentation.
