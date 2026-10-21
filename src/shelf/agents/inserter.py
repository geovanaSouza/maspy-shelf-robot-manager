from maspy import *


class Inserter(Agent):
    def __init__(self, agt_name):
        super().__init__(agt_name)
        self.add(Belief("bye"))

    @pl(gain, Belief("bye"))
    def bye(self, src):
        self.print(f"Bye from {self.my_name}")
        self.stop_cycle()