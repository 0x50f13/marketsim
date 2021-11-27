from marketsim.util.math import *

class Agent:
    def __init__(self, _lambda=0.5):
        """
         _lambda -- risk-aversion degree
        """ 
        self.x = 0
        self._lambda = _lambda
        self.w_history = []
        self.p_history = []
        self.d_history = []
        self.d_current = None
        self.p_current = None

    def set_parent(self, _parent): # parent: Market
        self.parent = _parent

    def w(self):
        return self.x*(self.p+self.d)-self.p_history[-1]*(1+self.parent.r)*(self.w_history[-1]-self.p_history[-1]*self.x)

    def _predict_price(self, d: float, p: float):
        pass

    def demand(self, d: float, p: float) -> float:
        """
            d -- t-th divident pf risky asset
            p -- price of risky asset
        """
        self.d_current = d
        self.p_current = p
        assert len(self.p_history) == len(self.d_history)
        if len(self.p_history) > 0:
            self.w_history.append(self.w())
        else:
            self.w_history.append(0.0) # FIXME: Research does not sepcify value of W_{i,0}
        Ep = self._predict_price(p,d)
        Xi = (Ep-p*(1+self.parent.r))/(self._lambda*self.parent.sigma2)
        #print("Agent expectation=",Ep)
        #print("Agent expectation of risk-free=",p*(1+self.parent.r))
        Xi = relu(Xi)
        self.x += Xi
        return Xi

    def __call__(self, d: float, p: float) -> float: # Magic warpper for demand
        return self.demand(p,d)

