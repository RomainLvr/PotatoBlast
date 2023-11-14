import os
import j2l.pytactx.agent as pytactx
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
                      arena="potatoblast", 
                      username="demo", 
                      password="demo", 
                      server="mqtt.jusdeliens.com"
                    )

def initArena():
    """
    Function that executes at launch.
    """
    arbitre.ruleArena("bgImg", "https://github.com/RomainLvr/PotatoBlast/blob/main/src/server/res/background.png?raw=true")
    arbitre.ruleArena("preview", "https://github.com/RomainLvr/PotatoBlast/blob/main/src/server/res/preview.png?raw=true")
    time.sleep(0.3)
    arbitre.update()

initArena()