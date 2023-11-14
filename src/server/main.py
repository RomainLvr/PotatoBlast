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
PASSWORD = os.getenv('PASSWORD')
SERVER = os.getenv('SERVER')
USERNAME = os.getenv('USERNAME')
ARENA = os.getenv('ARENA')
ARBITRE_USERNAME = os.getenv('ARBITRE_USERNAME')

# Création de l'arbitre
arbitre = pytactx.Agent(playerId=ARBITRE_USERNAME, 
                      arena=ARENA, 
                      username=USERNAME, 
                      password=PASSWORD, 
                      server=SERVER,
                      verbosity=2
                    )

def initArena():
    """
    Function that executes at launch.
    """
    arbitre.ruleArena("bgImg", "res/background.png")
    time.sleep(0.3)
    arbitre.update()

    map = copy.deepcopy(arbitre.game["map"])

    arbitre.ruleArena("map", map)
    time.sleep(0.3)
    arbitre.update()

initArena()