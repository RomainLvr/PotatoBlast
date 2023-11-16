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
    map = copy.deepcopy(arbitre.map)
    for row in map:
        for i in range(len(row)):
            if i <= 7 or i >= 32:
                row[i] = 1
            else : 
                row[i] = 0

    arbitre.ruleArena("map", map) 
    arbitre.ruleArena("mapImgs", [
                        "",
                        "none.png",
    ])   
    time.sleep(0.3)
    arbitre.update()

    agents =  {
        "joueur1": {
            "team": "0",
            "x": 24,
            "y": 27
        },
        "joueur2": {
            "team": "0",
            "x": 21,
            "y": 27
        },
        "joueur3": {
            "team": "0",
            "x": 18,
            "y": 27
        },
        "joueur4": {
            "team": "0",
            "x": 15,
            "y": 27
        },
    }

    for agentId, attributes in agents.items():
        for attributeKey, attributeValue in attributes.items():
            arbitre.rulePlayer(agentId, attributeKey, attributeValue)
    time.sleep(0.3)
    arbitre.update()

initArena()
