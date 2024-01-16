import main
import potatoes_arbiter
from threading import Thread

if __name__ == "__main__":
    # Lancement du serveur
    threadMain = Thread(target=main.run)
    threadMain.start()
    print("Server started")

    # Création du thread pour l'arbitre
    threadArbiter = Thread(target=potatoes_arbiter.run)
    threadArbiter.start()
    print("Potatoes arbiter started")

