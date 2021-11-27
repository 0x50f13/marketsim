from math import *

from marketsim.agent import Agent

class AnchoringAgent(Agent):
    def __init__(self, k=0.5, _lambda=0.5):
        super(AnchoringAgent, self).__init__(_lambda)
        self.k = k

    def _predict_price(self, p: float, d: float):
        if len(self.parent.price_history) < 10:
            return p  # To avoid dead market, where agents do not expect price changes ever
        k = self.k
        p_pr = self.parent.price_history
        d_pr = self.parent.d_history
        react = (1 - k) + 0.2*(sum([(p_pr[-1]+d_pr[-1])/(p_pr[-1]-i) - 1 for i in range(5)])) + k*0.2*(sum([(p_pr[-5]+d_pr[-5])/(p_pr[-5]-i) - 1 for i in range(5)]))
        return p*(1+react)+d*(1+react)
