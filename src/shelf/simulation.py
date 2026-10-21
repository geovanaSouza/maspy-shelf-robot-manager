from maspy import *

from shelf.agents.taker import Taker
from shelf.agents.inserter import Inserter
from shelf.environment import Shelf


def main():
    print(f"Initializing robots in an environment with shelves")

    # Define environment
    shelf = Shelf("Shelf")

    # Define Robots Agent
    taker = Taker("Taker")
    inserter = Inserter("Inserter", instant_mail=True)

    # Configure admin and system initialization
    Admin().connect_to([taker, inserter], shelf)
    Admin().start_system()
