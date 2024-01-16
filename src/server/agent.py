import j2l.pytactx.agent as pytactx

agent = pytactx.Agent(playerId="P1",
                        arena="potatoblast",
                        username="demo",
                        password="demo",
                        server="mqtt.jusdeliens.com"
                        )

while True:
    agent.move(1, 0)
    agent.update()