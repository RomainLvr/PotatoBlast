import sys
import os

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(src_path)

from api.j2l.pytactx import agent as pytactx
import os
import time
import copy

from dotenv import load_dotenv
load_dotenv()
AGENT_PASSWORD = os.getenv('__AGENT_PASSWORD__')
SERVER = os.getenv('__SERVER__')
USERNAME = os.getenv('__USERNAME__')
ARENA = os.getenv('__ARENA__')
ARBITRE_USERNAME = os.getenv('__ARBITRE_USERNAME__')

# Création de l'arbitre
arbitre = pytactx.Agent(playerId=ARBITRE_USERNAME, 
                      arena=ARENA, 
                      username=USERNAME, 
                      password=AGENT_PASSWORD, 
                      server=SERVER,
                      verbosity=2
                    )

def initArena():
    """
    Function that executes at launch. Modifies the rules
    to implement bomb rules, 
    then spawns 6 agents 
    """
    arbitre.ruleArena("bgImg", "backgrounds.png")
    time.sleep(0.3)
    arbitre.update()

    map = copy.deepcopy(arbitre.game["map"])

    arbitre.ruleArena("map", map)
    time.sleep(0.3)
    arbitre.update()

initArena()