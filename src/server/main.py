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
    # Set des options de la map
    arbitre.ruleArena("bgImg", "https://github.com/RomainLvr/PotatoBlast/blob/main/src/server/res/background.png?raw=true")
    arbitre.ruleArena("mapImgs", ["", "none.png",])  
    map = copy.deepcopy(arbitre.map)
    for row in map:
        for i in range(len(row)):
            if i <= 7 or i >= 32:
                row[i] = 1
            else : 
                row[i] = 0

    arbitre.ruleArena("map", map) 
    time.sleep(1)
    arbitre.update()

    # Set des profils et de leurs options
    arbitre.ruleArena("profiles", ["default", "arbitre", "potato"])
    arbitre.ruleArena(
        "spawnArea",
        {
            "x": [20, 0, 25, 15],
            "y": [27, 0, 27, 27],
            "r": [0, 0, 0, 0],
        }
    )
    arbitre.ruleArena("colisions", [True, True, True, True,])
    time.sleep(0.3)
    arbitre.update()
 
    arbitre.ruleArena("weapons", ["oil",])  
    arbitre.ruleArena("fireImgs", ["oil-drop.png",])  
    arbitre.ruleArena("infiniteAmmo", [False, False, False, False,])
    time.sleep(0.3)
    arbitre.update()

    for agentId, attributes in agents.items():
        for attributeKey, attributeValue in attributes.items():
            arbitre.rulePlayer(agentId, attributeKey, attributeValue)
    time.sleep(0.3)
    arbitre.update()

initArena()

# Boucle principale pour actualiser l'arbitre 
while True:
    # Changement d'orientation de l'arbitre pour montrer qu'il est actif dans l'arène
    arbitre.lookAt((arbitre.dir+1)%4)
    arbitre.update()