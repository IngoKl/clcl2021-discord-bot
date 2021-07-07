from string import Template
import random

import yaml

with open('data/templates.yml', 'r', encoding='utf8') as templates_file:
    templates = yaml.safe_load(templates_file)

def template(intent, entity=None):
    '''This is a very simple function that return 
    a random template for a given intent.'''

    # Check if there are templates for the intent
    if intent in templates.keys():

        # A list of suitable templates
        template_options = []

        for to in templates[intent]:

            # Only add entity-based templates if there's one
            entity_based = '$entity' in to
            
            if not entity_based:
                template_options.append(to)

            if entity_based and entity:

                # Fill template with entity
                to = Template(to).substitute(entity=entity)

                template_options.append(to)

    
        # Select a random template from the options
        return random.choice(template_options)

    else:
        return False