from maspy import *


class Shelf(Environment):
    def __init__(self, env_name=None):
        super().__init__(env_name)
        self.create(percept=Percept("object"))

    def take(self, agt):
        self.print(f"Agent {agt} is taking object")
        object = self.get(Percept("object"))
        # WORKAROUND: this delete should make the Inserter lose its belief in
        # the object and trigger @pl(lose, Belief("object_exist")). In maspy
        # 2026.5.13 the Percept lose event is not matched against Belief
        # triggers, so Taker sends a tell/untell pair instead (see taker.py).
        self.delete(object)