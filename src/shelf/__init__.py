"""Shelf robot manager MAS built with Maspy."""

from shelf.agents.taker import Taker
from shelf.agents.inserter import Inserter
from shelf.environment import Shelf
from shelf.simulation import main

__all__ = ["Shelf", "Taker", "Inserter", "main"]
