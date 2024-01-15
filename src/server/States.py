import random


class Up:
    def handle(self, potato):
        x = potato.potato["x"]
        y = potato.potato["y"]
        if y <= 2:
            potato.change_state(Down())
        else:
            randomInt = random.randint(-1, 1)
            while not (4 < x + randomInt < 15):
                randomInt = random.randint(-1, 1)
            potato.arbiter.rulePlayer(potato.potato["clientId"], "x", x + randomInt)
            potato.arbiter.rulePlayer(potato.potato["clientId"], "y", y - 1)
            potato.potato.update()


class Down:
    def handle(self, potato):
        x = potato.potato["x"]
        y = potato.potato["y"]
        if y >= 14:
            potato.change_state(Up())
        else:
            randomInt = random.randint(-1, 1)
            while not (4 < x + randomInt < 15):
                randomInt = random.randint(-1, 1)
            potato.arbiter.rulePlayer(potato.potato["clientId"], "x", x + randomInt)
            potato.arbiter.rulePlayer(potato.potato["clientId"], "y", y + 1)
            potato.potato.update()


class Center:
    def handle(self, potato):
        # Réinitialiser l'état de la patate
        potato.arbiter.rulePlayer(potato.potato["clientId"], "x", 9)  # Centre en x
        potato.arbiter.rulePlayer(potato.potato["clientId"], "y", 8)
        potato.potato.update()
        x = potato.potato["x"]
        y = potato.potato["y"]
        if 9 >= y >= 7:
            potato.change_state(Down())