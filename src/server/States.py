# Implémentation des états concrets
import math


# Implémentation des états concrets
class Up:
    def handle(self, potato):
        print("Handle Up")
        x = potato.potato["x"]
        y = potato.potato["y"]
        if y == 2:
            potato.change_state(Down())
        else:
            potato.arbiter.rulePlayer(potato.potato["clientId"], "y", y - 1)
            potato.potato.update()


class Down:
    def handle(self, potato):
        print("Handle Down")
        x = potato.potato["x"]
        y = potato.potato["y"]
        if y == 14:
            potato.change_state(Up())
        else:
            potato.arbiter.rulePlayer(potato.potato["clientId"], "y", y + 1)
            potato.potato.update()


class Center:
    def handle(self, potato):
        print("Handle Center")
        # Réinitialiser l'état de la patate
        potato.arbiter.rulePlayer(potato.potato["clientId"], "x", 9)  # Centre en x
        potato.arbiter.rulePlayer(potato.potato["clientId"], "y", 8)
        potato.potato.update()
        potato.change_state(Down())
