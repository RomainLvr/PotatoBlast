import time
import src.server.j2l.pytactx.agent as pytactx
import src.server.main_powerups as main_powerups
agent = pytactx.AgentFr(nom="chen zen", arene="potatoblast", username="demo",password="demo", url="mqtt.jusdeliens.com", verbosite=3)

referee_powerups = pytactx.Agent(playerId="francis_saucisse",
                        arena="potatoblast",
                        username="demo",
                        password="demo",
                        server="mqtt.jusdeliens.com"
                        )

active_powerups={"invincibility":False,"freeze":False,"doubleShoot":False}
agent = pytactx.AgentFr(nom="chen zen", arene="potatoblast", username="demo",password="demo", url="mqtt.jusdeliens.com", verbosite=3)

def test_death():
    """ Test if an agent that gets hit by a potato gets his score reset and respawns """
    
    agent.death()
    time.sleep(agent.dtRespawn*1000)
    assert agent.score==0,"the score of the agent must be reset after dying"
    assert agent.invincible==True,"The agent must be invincible when spawning"
    time.sleep(900)
    assert agent.invincible==True,"The respawn invincibility frame has not yet been elapsed"
    time.sleep(101)
    assert agent.invincible==False,"The 1 second of respawn invincibility is elapsed"

def test_invincibilityPowerup():
    """Tests that the invincibility powerup works correctly"""
    
    main_powerups.activatePowerUp("invincibility")
    assert agent.invincible==True,"The agent must be invincible for 10 seconds "
    print("Waiting for the powerup to consume...")
    time.sleep(9500)
    assert agent.invincible==True,"The invincibility powerup has not been elapsed yet"
    time.sleep(501)
    assert agent.invincible==False,"The invincibility powerup has been elapsed"

def test_doubleShootPowerup():
    """Tests that the double shoot powerup works correctly"""
    
    main_powerups.activatePowerUp("doubleShoot")
    assert agent.doubleShoot==True,"The agent must shoot 2 bullets instead of 1"
    print("Waiting for the double shoot powerup to consume...")
    time.sleep(9500)
    assert agent.doubleShoot==True,"The double shoot  powerup has not been elapsed yet"
    time.sleep(501) 
    assert agent.doubleShoot==False,"The double shoot powerup has been elapsed"

def test_freezePowerup():
    """Tests that the freeze powerup works correctly and that the potatoes are not able to move"""
    main_powerups.activatePowerUp("freeze")
    
    for ptt in referee_powerups.range:
        if ptt.profiles==2:  
            assert ptt.speedMax==0, "A potato is able to move"

    print("Waiting for the freeze powerup to consume...")
    time.sleep(9500)
    for ptt in referee_powerups.range:
        if ptt.profiles==2:
            assert ptt.speedMax==0, "A potato is able to move, the freeze powerup has not been elapsed yet"
    time.sleep(501)
    for ptt in referee_powerups.range:
        if ptt.profiles==2:
            assert ptt.speedMax==0, "A potato is not able to move though the freeze powerup has been elapsed"

def test_potatoDestroyed():
    while referee_powerups.range[i].profiles!=2:
        testPotato=referee_powerups.range[i]
        i=i+1
    if referee_powerups.range[i].profiles==2:
        testPotato.life==0
        assert testPotato.life==testPotato.maxLife,"The destroyed potato has not been respawned correctly"
    else:
        print("No potato found")
    testPotato.life==0
    assert testPotato.life==testPotato.maxLife,"The destroyed potato has not been respawned correctly"


def test_score():
    """Tests that the score is correctly incremented when a potato is destroyed"""
    i=0
    while referee_powerups.range[i].profiles!=2:
        testPotato=referee_powerups.range[i]
        i=i+1
    if referee_powerups.range[i].profiles==2:
        testPotato.life==0
        assert agent.score==1,"The score has not been incremented after destroying a potato"
    else:
        print("No potato found")

def main():
    test_potatoDestroyed()
    test_death()
    test_invincibilityPowerup()
    test_doubleShootPowerup()
    test_freezePowerup()
    

