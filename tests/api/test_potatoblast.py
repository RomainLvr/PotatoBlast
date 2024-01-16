import src.server.j2l.pytactx.agent as pytactx


agent = pytactx.AgentFr(nom="chen zen", arene="potatoblast", username="demo",password="demo", url="mqtt.jusdeliens.com", verbosite=3)

def test_move_left():
    """Tests that the fryer is able to move to the left"""
    currentX = agent.x
    if(agent.x==20 or agent.x==0):
        agent.x=10
    agent.moveLeft()
    assert agent.x == currentX-1, "The agent has not moved to the left"

    agent.x=0
    agent.moveLeft()
    assert agent.x == 0, "The agent should not be able to move to the left when he is at the edge of the map"

def test_move_right():
    """Tests that the fryer is able to move to the left"""
    currentX = agent.x
    if(agent.x==20 or agent.x==0):
        agent.x=10
    agent.moveRight()
    assert agent.x == currentX+1, "The agent has not moved to the right"

    agent.x=20
    agent.moveRight()
    assert agent.x == 0, "The agent should not be able to move to the right when he is at the edge of the map"