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
urlBase = "https://raw.githubusercontent.com/RomainLvr/PotatoBlast/main/src/server/res/"


def initArena():
    """
    Function that executes at launch.
    """
    # Set des options de la map
    arbitre.ruleArena("gridColumns", 20)
    arbitre.ruleArena("gridRows", 16)
    arbitre.ruleArena("bgImg",
                      urlBase + "background.png?raw=true")
    arbitre.ruleArena("mapFriction", [0, 1])
    arbitre.ruleArena("mapBreakable", [False, False])
    arbitre.ruleArena("mapHit", [0, 0])
    map = copy.deepcopy(arbitre.map)
    for row in map:
        for i in range(len(row)):
            if i == 3 or i == 16:
                row[i] = 1
            else:
                row[i] = 0
    map[0][0] = 0

    arbitre.ruleArena("map", map)

    # Set des profils et de leurs options
    arbitre.ruleArena(
        "profiles",
        [
            "default",
            "arbitre",
            "potato",
        ]
    )

    arbitre.ruleArena(
        "pImgs",
        [
            urlBase + "fryerPlayer.png",
            urlBase + "referee.png",
            urlBase + "potato_1.png",
        ]
    )

    arbitre.ruleArena(
        "pIcons",
        [
            "🍟",
            "👮",
            "🥔"
        ]
    )

    time.sleep(0.5)
    arbitre.update()

    arbitre.ruleArena(
        "spawnArea",
        {
            "x": [10, 100, 10],
            "y": [14, 100, 0],
            "r": [0, 0, 0],
        }
    )
    arbitre.ruleArena(
        "colisions",
        [ 
            False,
            False,
            True,
        ]
    )
    
    profileRange = arbitre.game["range"]
    profileRange[0] = 0
    profileRange[1] = 0
    profileRange[2] = 0
    arbitre.ruleArena(
        "range",
        profileRange
    )

    arbitre.ruleArena("score", "DM")
    arbitre.ruleArena("maxPlayers", 10)
    arbitre.ruleArena("maxRobots", 10)
    time.sleep(0.5)
    arbitre.update()

    weapons = [
        "nothing",
        "oil"
    ]
    arbitre.ruleArena(
        "weapons",
        weapons
    )
    time.sleep(0.5)
    arbitre.update()
    arbitre.ruleArena(
        "wIcons",
        [
            "",
            "💧",
        ]
    )
    arbitre.ruleArena(
        "bullet",
        [-1, -1]
    )
    arbitre.ruleArena(
        "fireImgs",
        [
            "",
            urlBase + "oil.png",
        ]
    )
    arbitre.ruleArena(
        "weapon",
        [1, 0, 0]
    )

    arbitre.ruleArena(
        "dtFire",
        [300,300]
    )
    arbitre.ruleArena(
        "hitFire",
        [0,10]
    )
    arbitre.ruleArena(
        "ownerFire",
        [False,False]
    )
    arbitre.ruleArena(
        "rangeFire",
        [0,5]
    )
    arbitre.ruleArena(
        "spreadFire",
        [0,0]
    )
    arbitre.ruleArena(
        "accelerationFire",
        [0,0]
    )
    
    arbitre.ruleArena("infiniteAmmo", [True, True, True, ])
    arbitre.ruleArena("dtMove", [250, 10, 1000, ])
    arbitre.ruleArena("collision", [False, False, True, ])

    arbitre.ruleArena(
        "teamColors",
        {
            [255, 218, 51],
            [0, 0, 0],
        }
    )
    arbitre.ruleArena("teamNb", 2)
    arbitre.ruleArena("teamName", ["🍟", "🥔"])
    time.sleep(0.3)
    arbitre.update()


initArena()
initArena()
arbitre.moveTowards(18,0)
agent = pytactx.Agent(playerId="P1",
                        arena="potatoblast",
                        username="demo",
                        password="demo",
                        server="mqtt.jusdeliens.com"
                        )

# Boucle principale pour actualiser l'arbitre 
while True:
    # arbitre.ruleArena("info", "testest")
    newRange = copy.deepcopy(arbitre.range)

    score = 0

    if oldRange != newRange:

        for player, playerStats in newRange.items():
            if playerStats["profile"] != 0:
                continue
            # If a player orientation is different from 0, its forced to 0.
            if playerStats["reqDir"] != 1 or playerStats["dir"] != 1:
                arbitre.rulePlayer(playerStats["clientId"], "reqDir", 1)
            # If a player want to move to the top or to the bottom, he is forced to stay in the middle.
            if playerStats["reqY"] != 14 or playerStats["y"] != 14:
                arbitre.rulePlayer(playerStats["clientId"], "reqY", 14)
            # If a player is dead, he is respawned but his score is reset.
            if playerStats["life"] <= 0:
                arbitre.rulePlayer(playerStats["clientId"], "score", 0)

            # Update total score of the game
            score += playerStats["score"]
    infoScores = " 🏆 Total SCORE : " + str(score) + " 🏆"
    arbitre.ruleArena("info", infoScores)

    oldRange = newRange
    arbitre.update()

    agent.fire(True)
    agent.update()
