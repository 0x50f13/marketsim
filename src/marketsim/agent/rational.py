from agent import Agent
from math import *

class RationalAgent(Agent):
    def _predict_price(self, p: float, d: float):
        return self.parent.rho*(self.parent.g + d) + (1 - self.parent.rho)*floor((1 + self.parent.f)*self.parent.d+self.parent.g)
