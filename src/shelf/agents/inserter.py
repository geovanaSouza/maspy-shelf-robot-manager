from maspy import *


class Inserter(Agent):
    # WORKAROUND: this plan is triggered by Taker's untell of the mirrored
    # "object_exist" belief, not by the Shelf deleting Percept("object"). The
    # environment lose event should trigger it too, but in maspy 2026.5.13 a
    # Percept lose does not match a Belief trigger.
    @pl(lose, Belief("object_exist"))
    def insert_obj(self, src):
        self.print(f"[{self.cycle_counter}] Need to ressuply a new object (src={src})")
        self.stop_cycle()