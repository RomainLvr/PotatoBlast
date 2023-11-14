import time


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
    agent.invincibilityPowerup()
    assert agent.invincible==True,"The agent must be invincible for 10 seconds "
    print("Waiting for the powerup to consume...")
    time.sleep(9500)
    assert agent.invincible==True,"The invincibility powerup has not been elapsed yet"
    time.sleep(501)
    assert agent.invincible==False,"The invincibility powerup has been elapsed"

def test_doubleShootPowerup():
    """Tests that the double shoot powerup works correctly"""
    agent.doubleShootPowerup()
    assert agent.doubleShoot==True,"The agent must shoot 2 bullets instead of 1"
    print("Waiting for the double shoot powerup to consume...")
    time.sleep(9500)
    assert agent.doubleShoot==True,"The double shoot  powerup has not been elapsed yet"
    time.sleep(501) 
    assert agent.doubleShoot==False,"The double shoot powerup has been elapsed"

def test_freezePowerup():
    """Tests that the freeze powerup works correctly"""
    agent.freezePowerup()
    for ptt in potatoes:
        assert ptt.canMove==False, "A potato is able to move"
    print("Waiting for the freeze powerup to consume...")
    time.sleep(9500)
    for ptt in potatoes:
        assert ptt.canMove==False, "A potato is able to move, the freeze powerup has not been elapsed yet"
    time.sleep(501)
    for ptt in potatoes:
        assert ptt.canMove==True, "A potato is not able to move, the freeze powerup has been elapsed"

def test_potatoDestroyed():
    testPotato=potatoes[0]
    testPotato.life==0
    assert testPotato.life==testPotato.maxLife,"The destroyed potato has not been respawned correctly"


def main():
    test_death()
    test_invincibilityPowerup()
    test_doubleShootPowerup()
    test_freezePowerup()
    test_potatoDestroyed()

