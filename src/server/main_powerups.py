import os
from random import randint
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


referee_powerups = pytactx.Agent(playerId="francis_saucisse",
                        arena="potatoblast",
                        username="demo",
                        password="demo",
                        server="mqtt.jusdeliens.com"
                        )

active_powerups={"invincibility":False,"freeze":False,"doubleShoot":False}

def activatePowerUp(powerup):
    active_powerups[powerup]=True
    checkPowerUps()
    time.sleep(5)
    active_powerups[powerup]=False
    checkPowerUps()


def checkPotatoDeath():
    for agent in referee_powerups.range:
        if agent.profiles==2:
            if(agent.life==0):
                rand=randint(0,10)
                match rand:
                    case 0:
                        activatePowerUp("invincibility")
                    case 1:
                        activatePowerUp("freeze")
                    case 2:
                        activatePowerUp("doubleShoot")
                    default:
                        break

def checkPowerUps():
    fryers=[]
    potatoes=[]
    for agent in referee_powerups.range:
        if agent.profiles==0:
            fryers+=agent
        else:
            if agent.profile==2:
                potatoes+=agent
    
    for agent in fryers:
        if active_powerups["invincibility"] and not agent.invincible or not active_powerups["invincibility"] and agent.invincible:
            agent.invincible= not agent.invincible

        if active_powerups["doubleShoot"] and agent.dtFire==2000 or not active_powerups["doubleShoot"] and agent.dtFire==4000:
            divider=1
            if not agent.doubleShootPowerup:
                    divider+=1
            agent.dtFire=4000/divider

        if active_powerups["freeze"] and potatoes[0].speedMax!=0:
            for potato in potatoes:
                potato.speedMax=0
        else:
            if not active_powerups["freeze"] and potatoes[0].speedMax==0:
                for potato in potatoes:
                    potato.speedMax=potato.speedIni

