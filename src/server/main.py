# import of standard libraries
import time
import os
import json

# File directory definition
__fileDir__ = os.path.dirname(os.path.abspath(__file__))

# ENV variables config
from dotenv import load_dotenv
load_dotenv()
ARBITRE=os.getenv('ARBITRE')
ARENA=os.getenv('ARENA')
USERNAME=os.getenv('USERNAME')
PASSWORD=os.getenv('PASSWORD')
SERVER=os.getenv('SERVER')
PORT=int(os.getenv('PORT'))
DURATION=int(os.getenv('DURATION'))

# # Import referee class and utils
from referee import Referee
from utils import *

# # Import json rules file
try:
    with open(os.path.join(__fileDir__, 'serverParameter.json')) as json_data:
        serverRulesdict = json.load(json_data)
except Exception as e:
    print(f"Une erreur est survenue dans le chargement des données : {e}")

# # Referee creation
referee = Referee(ARBITRE, ARENA, USERNAME, PASSWORD, SERVER, PORT, DURATION)
referee.printInfoToArena("⌛ Initialisation de l'arbitre...")

# # Reset arena
referee.resetArena()
referee.update()
time.sleep(3)
referee.update()

referee.setRefereeMap(referee.getGameInfos()["map"])
referee.update()
time.sleep(0.3)

referee.setArenaRules(serverRulesdict)
referee.update()
time.sleep(1)

referee.update()