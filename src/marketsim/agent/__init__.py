class Agent:
    def __init__(self):
        self.x = 0

    def set_parent(self, _parent): # parent: Market
        self.parent = _parent

    def demand(self, d: float, p: float) -> float:
        """
            d -- t-th divident pf risky asset
            p -- price of risky asset
        """
        pass

    def __call__(self, d: float, p: float -> float: # Magic warpper for demand
        return self.demand(d, p)    

