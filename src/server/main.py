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
oldRange = {}
newRange = {}


def initArena():
    """
    Function that executes at launch.
    """
    # Set des options de la map
    arbitre.ruleArena("gridColumns", 20)
    arbitre.ruleArena("gridRows", 16)
    arbitre.ruleArena("bgImg",
                      "https://github.com/RomainLvr/PotatoBlast/blob/main/src/server/res/background.png?raw=true")
    arbitre.ruleArena(
        "mapImgs",
        [
            "",
            "",
            "https://raw.githubusercontent.com/RomainLvr/PotatoBlast/main/src/server/res/referee.png",
        ]
    )
    arbitre.ruleArena("mapFriction", [0, 1, 2, 3, 4])
    map = copy.deepcopy(arbitre.map)
    for row in map:
        for i in range(len(row)):
            if i <= 3 or i >= 16:
                row[i] = 1
            else:
                row[i] = 0
    map[0][0] = 0

    arbitre.ruleArena("map", map)
    time.sleep(1)
    arbitre.update()

    # Set des profils et de leurs options
    arbitre.ruleArena("profiles", ["default", "arbitre", "potato"])
    arbitre.ruleArena(
        "spawnArea",
        {
            "x": [10, 0, 10],
            "y": [14, 0, 14],
            "r": [0, 0, 0],
        }
    )
    arbitre.ruleArena("colisions", [False, False, False, ])
    arbitre.ruleArena("pImgs", ["https://raw.githubusercontent.com/RomainLvr/PotatoBlast/main/src/server/res/fryer.png",
                                "https://raw.githubusercontent.com/RomainLvr/PotatoBlast/main/src/server/res/potato_6.png",
                                "", ])
    arbitre.ruleArena("range", [0, 0, 0])
    time.sleep(0.3)
    arbitre.update()

    arbitre.ruleArena("weapons", ["", "oil", ])
    arbitre.ruleArena("fireImgs", ["",
                                   "https://raw.githubusercontent.com/RomainLvr/PotatoBlast/main/src/server/res/oil-drop.png", ])
    arbitre.ruleArena("infiniteAmmo", [True, True, True, ])
    arbitre.ruleArena("dtMove", [150, 10, 150, ])
    time.sleep(0.3)
    arbitre.update()


initArena()
# Boucle principale pour actualiser l'arbitre 
while True:
    # Changement d'orientation de l'arbitre pour montrer qu'il est actif dans l'arène
    arbitre.lookAt((arbitre.dir + 1) % 4)
    # arbitre.ruleArena("info", "testest")
    newRange = copy.deepcopy(arbitre.range)

    score = 0

    if oldRange != newRange:



        for player, playerStats in newRange.items():

            # If a player orientation is different from 0, its forced to 0.
            if playerStats["reqDir"] != 1 or playerStats["dir"] != 1:
                arbitre.rulePlayer(playerStats["clientId"], "reqDir", 1)
            # If a player want to move to the top or to the bottom, he is forced to stay in the middle.
            if playerStats["reqY"] != 14 or playerStats["y"] != 14:
                arbitre.rulePlayer(playerStats["clientId"], "reqY", 14)
            # If a player is dead, he is respawned but his score is reset.
            if playerStats["life"] >= 0:
                arbitre.rulePlayer(playerStats["clientId"], "score", 10)

            # Update total score of the game
            score += playerStats["score"]

    infoScores = "Total SCORE : " + str(score)
    arbitre.ruleArena("info", infoScores)

    oldRange = newRange
    arbitre.update()
    time.sleep(0.3)

    # If a team wins,
    # The game is paused
