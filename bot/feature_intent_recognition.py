from numpy import conjugate
import spacy

def pizza_intent(message_text):
    '''This is modeled after Vasiliev 2020, Chapter 8.'''

    # This is not a language independent bot
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(message_text)

    dobj = None
    verb = None

    for token in doc:
        if token.dep_ == 'dobj':
            dobj = token.text
            verb = token.head.text

    if dobj and verb:
        # The first item in each list will be the 'canonical' form
        verb_list = [('order', 'want', 'give', 'make', 'get', 'take'), ('show', 'hand', 'find')]
        verb_syns = [item for item in verb_list if verb in item]
        
        dobj_list = [('pizza', 'pie', 'dish', 'slice'), ('coke', 'soda', 'pop'), ('menu', 'options', 'offers')]
        dobj_syns = [item for item in dobj_list if dobj in item]

        intent = f'{verb_syns[0][0]}_{dobj_syns[0][0]}'
        
        ''' The options are: 
        order_pizza, order_coke, order_menu, show_pizza, show_coke, show_menu
        We will not limit the options and provide the but with the intent.
        '''

        if 'menu' in intent:
            return 'pizza_menu'
        if 'pizza' in intent:
            return 'pizza_order'
        if 'coke' in intent:
            return 'coke_order'
    
    else:
        return False