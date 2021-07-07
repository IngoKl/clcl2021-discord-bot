import random


class CashierDialogueFSM:
    '''This is a FSM (well, basically) that handles a baisc dialogue.'''

    def __init__(self, customer):
        # This will be the name of our conversation partner
        self.customer = customer
        self.current_state = self.state_greet
        self.total = random.uniform(1, 10)
        self.finished = False

    def handle_message(self, message):

        if message == 'Bye':
            self.current_state = self.state_thanks_bye

        return self.current_state(message)

    def state_greet(self, message):
        self.current_state = self.state_ask_coupons

        return f'Welcome {self.customer}, how are you doing today?'

    def state_announce_total(self, message):
        self.current_state = self.state_decide_payment_method

        return f'That will be ${round(self.total, 2)} then. How will you be paying today?'

    def state_has_coupons(self, message):

        self.total = self.total * 0.9

        self.current_state = self.state_announce_total
        return 'Great, that coupon will save you some money! ' + self.current_state(message)

    def state_ask_coupons(self, message):
        self.current_state = self.state_decide_coupons

        return f'Your total comes to ${round(self.total, 2)}. Do you happen to have any coupons?'

    def state_decide_coupons(self, message):
        if 'no' in message.lower():
            return self.state_announce_total(message)
        if 'yes' in message.lower():
            self.current_state = self.state_has_coupons
            return self.current_state(message)

        self.current_state = self.state_ask_coupons
        return self.current_state(message)

    def state_decide_payment_method(self, message):
        if 'cash' in message.lower():
            self.current_state = self.state_question
            return 'Fantastic. Here is your change! Is there anything else?'
        if 'card' in message.lower():
            self.current_state = self.state_question
            return 'Great, I just need you to swipe your card. Is there anything else?'

        self.current_state = self.state_announce_total
        return self.current_state(message)

    def state_handle_questions(self, message):
        self.current_state = self.state_question

        return 'Thank you for pointing this out! Is there anything else?'

    def state_question(self, message):
        if 'no' in message.lower():
            self.current_state = self.state_thanks_bye
            return self.current_state(message)
        else:
            self.current_state = self.state_handle_questions
            return self.current_state(message)

    def state_thanks_bye(self, message):
        # Reset
        self.current_state = self.state_greet
        self.finished = True

        return 'Thank you! Have a wonderful day!'

