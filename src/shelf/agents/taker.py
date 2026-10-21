from maspy import *


class Taker(Agent):
    def __init__(self, agt_name):
        super().__init__(agt_name)
        self.add(Goal("take_object"))
        

    @pl(gain, Goal("take_object"))
    def take_object(self, src):
        self.print(f"[{self.cycle_counter}] Takin object")
        # WORKAROUND: Shelf.take() deletes the object Percept, but that lose
        # event does not trigger Inserter's @pl(lose, Belief("object_exist"))
        # in maspy 2026.5.13. Mirror the object as a Belief and remove it via
        # untell so Inserter receives a Belief lose event instead.
        self.send(broadcast, tell, Belief("object_exist"))
        self.take()
        self.send(broadcast, untell, Belief("object_exist"))
        self.stop_cycle()