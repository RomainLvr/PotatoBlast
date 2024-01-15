import random

import j2l.pytactx.agent as pytactx
import os
from Potato import Potato

from dotenv import load_dotenv

from src.server import States

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

potatoes = []


# Création des potatos
def createPotato(lvl: int):
    if 1 <= lvl <= 8:
        rand = random.randint(0, 100 * lvl)
        agents = {
            "potato" + str(rand) + "_" + str(lvl): {
                "x": random.randint(4, 12),
                "y": random.randint(0, 3),
                "profile": 1 + lvl,
            },
        }
        for agentId, attributes in agents.items():
            for attributeKey, attributeValue in attributes.items():
                arbitre.rulePlayer(agentId, attributeKey, attributeValue)
        arbitre.update()
        potato = getPotatoById("potato" + str(rand) + "_" + str(lvl))
        if potato is not None:
            potatoes.append(Potato(potato, arbitre))


def complete_potatoes(potatoes, nb):
    missing_potatoes = nb - len(potatoes)

    for i in range(missing_potatoes):
        print("Creating potato")
        # Génère un niveau aléatoire entre 1 et 8 avec une notion de rareté (plus le niveau est élevé, plus il est rare)
        lvl = random.randint(1, 8)
        createPotato(lvl)  # Supposons que cette fonction crée une potato avec le niveau donné


def getPotatoById(id: str):
    for potato in arbitre.range.items():
        if potato[0] == id:
            return potato[1]
    return None


def isAgentInPotatoes(agentId: str):
    for potato in potatoes:
        if potato.potato["clientId"] == agentId:
            return True
    return False


nb_potatoes_demandees = 1  # Nombre total de potatoes demandées
arbitre.moveTowards(0, 0)
arbitre.lookAt(0)
arbitre.update()

# delete potatoes
for agent in arbitre.range.items():
    agentId = agent[0]
    if agentId.startswith("potato"):
        arbitre.rulePlayer(agentId, "life", 0)
        arbitre.update()

# Boucle principale pour actualiser l'arbitre
while True:
    for agent in arbitre.range.items():
        agentId = agent[0]
        if agentId.startswith("potato"):
            if not isAgentInPotatoes(agentId):
                potatoes.append(Potato(agent[1], arbitre))

    for potato in potatoes:
        if "clientId" in potato.potato:
            agentId = potato.potato["clientId"]
            x = potato.potato["x"]
            y = potato.potato["y"]
            if (y > 15 or y < 2 or x < 4 or x > 15) and not potato.state.__class__.__name__ == "Center":
                potato.change_state(States.Center())
            else:
                potato.update()

    complete_potatoes(potatoes, nb_potatoes_demandees)

    arbitre.update()
