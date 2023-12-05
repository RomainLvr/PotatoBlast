import os
import random

import j2l.pytactx.agent as pytactx
import os
import time
import copy
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


# Création des potatos
def createPotato(lvl: int):
    if 1 <= lvl <= 8:
        agents = {
            "potato" + str(lvl): {
                "x": random.randint(4, 12),
                "y": random.randint(0, 3),
                "profile": 2,
            },
        }
        for agentId, attributes in agents.items():
            for attributeKey, attributeValue in attributes.items():
                arbitre.rulePlayer(agentId, attributeKey, attributeValue)
        arbitre.update()
        potatoes.append(Potato(agents["potato" + str(lvl)], arbitre))


def complete_potatoes(potatoes, nb):
    # Compléter le nombre de potatoes manquantes en fonction du nombre de potatoes déjà présentes et du nombre de potatoes demandées en paramètre
    missing_potatoes = nb - len(potatoes)

    for i in range(missing_potatoes):
        # Génère un niveau aléatoire entre 1 et 8 avec une notion de rareté (plus le niveau est élevé, plus il est rare)
        lvl = random.randint(1, 8)
        createPotato(lvl)  # Supposons que cette fonction crée une potato avec le niveau donné


nb_potatoes_demandees = 1  # Nombre total de potatoes demandées
arbitre.moveTowards(0, 0)
arbitre.lookAt(0)
arbitre.update()

# Boucle principale pour actualiser l'arbitre
while True:

    potatoes = []
    for agent in arbitre.range.items():
        agentId = agent[0]
        if agentId.startswith("potato"):
            potatoAgent = Potato(agent[1], arbitre)
            potatoes.append(potatoAgent)

    complete_potatoes(potatoes, nb_potatoes_demandees)

    for potatoe in potatoes:
        agentId = potatoe.potatoId
        print(agentId)
        if agentId.startswith("potato"):
            x = potatoe["x"]
            y = potatoe["y"]
            if y == 15:
                if 4 < x > 12:
                    potatoe.change_state(States.Up())
            else:
                potatoe.change_state(States.Down())

        potatoe.potato.update()

    arbitre.update()
