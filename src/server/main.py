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
P3 = pytactx.Agent(playerId="P3",
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
            "",
        ]
    )
    arbitre.ruleArena("mapFriction", [0, 1, 2, 3, 4])
    map = copy.deepcopy(arbitre.map)
    for row in map:
        for i in range(len(row)):
            if i == 0 or i == 19:
                row[i] = 0
            elif i <= 3 or i >= 16:
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
            "y": [14, 0, 0],
            "r": [0, 0, 0],
        }
    )
    arbitre.ruleArena("colisions", [False, False, False, ])
    arbitre.ruleArena("pImgs", ["https://raw.githubusercontent.com/RomainLvr/PotatoBlast/main/src/server/res/fryerPlayer.png",
                                "https://raw.githubusercontent.com/RomainLvr/PotatoBlast/main/src/server/res/referee.png",
                                ""])
    arbitre.ruleArena("range", [0, 0, 0])
    arbitre.ruleArena("score", "")
    arbitre.ruleArena("nPlayers", 3)
    arbitre.ruleArena("maxPlayers", 3)
    arbitre.ruleArena("maxRobots", 10)
    time.sleep(0.3)
    arbitre.update()

    arbitre.ruleArena("weapons", ["", "oil", ""])
    arbitre.ruleArena("weapon", [1,2,0])
    arbitre.ruleArena("fireImgs", ["",
                                   "https://raw.githubusercontent.com/RomainLvr/PotatoBlast/main/src/server/res/oil-drop.png",
                                   ""])
    arbitre.ruleArena("infiniteAmmo", [True, True, True, ])
    arbitre.ruleArena("dtMove", [150, 10, 150, ])
    arbitre.ruleArena("dtFire", [2000, 500, 2000, ])
    arbitre.ruleArena("collision", [False, False, True, ])
    time.sleep(0.3)
    arbitre.update()


initArena()
# Boucle principale pour actualiser l'arbitre 
while True:
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
            if playerStats["life"] > 0:
                arbitre.rulePlayer(playerStats["clientId"], "score", 10)

            # Update total score of the game
            score += playerStats["score"]

    infoScores = "Total SCORE : " + str(score)
    arbitre.ruleArena("info", infoScores)

    oldRange = newRange
    arbitre.update()
    P3.fire(True)
    P3.update()
    time.sleep(0.3)

    # If a team wins,
    # The game is paused
