import yaml
import sys
from pathlib import Path

from bot.clcl_bot import CLCL2021Client

if __name__ == "__main__":

    # Loading the config YAML file
    if len(sys.argv) > 1:
        config_file = sys.argv[1]
    else:
        config_file = 'default.yml'

    with open(Path('config/' + config_file), 'r') as config_file:
        config = yaml.safe_load(config_file.read())


    # This will start the actual bot
    bot_client = CLCL2021Client()
    bot_client.run(config['token'])
