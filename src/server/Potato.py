import j2l.pytactx.agent as pytactx
import States


# Classe principale de l'agent
class Potato:
    def __init__(self, potato, arbiter):
        self.arbiter = arbiter
        self.potato = potato
        self.state = States.Down()

    # function to change the state of the agent
    # @param new_state the new state of the agent
    def change_state(self, new_state):
        if self.state.__class__.__name__ != new_state.__class__.__name__:  # Vérifiez si l'état change
            self.state = new_state
            print("New state: " + self.state.__class__.__name__)
            self.update()

    def get_state(self):
        return self.state

    # function to handle the state of the agent
    def update(self):
        print("Call " + self.get_state().__class__.__name__)
        self.get_state().handle(self)
