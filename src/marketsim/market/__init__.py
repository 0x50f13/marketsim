import random

class Market:
    def __init__(self, d: float, r=0.1, sigma2=0.0734, rho=0.95, f=6.333, g=16.688):
        """
            r -- risk-free asset rate
            d -- mean of AR process for divdends of risky asset
            sigma2 -- conditional variance of divedend process
            rho -- exogenous parameter
            f -- const
            g -- const
        """
        self.d = d
        self.r = r
        self.sigma2 = sigma2
        self.f = f
        self.g = g
        self.rho = rho
        self.agents = []
        self.demand_history = []
        self.demand = 0.0
        self.d_current = random.normalvariate(self.d, self.sigma2) # From https://python.quantecon.org/ar1_processes.html
        self.fair_price = 1.0
        self.demand_factor = 0.001
    def add_agent(self, agent):
        agent.set_parent(self)
        self.agents.append(agent)

    def get_dividends(self):
        # NOTE: Shoould be called ONCE per simulation iteration
        # NOTE: \mu undefined in research, so assuming \mu=1
        self.d_current = self.d + self.rho*(self.d_current-self.d)+random.normalvariate(0, self.sigma2)
        return self.d_current

    def get_price(self): 
        d = self.get_dividends()
        return d+self.fair_price+self.demand_factor*self.demand

    def simulate(self):
        """
         Simulates one iteration of market
        """ 
        p = self.get_price()
        print("price=",p)
        demand_current = 0.0
        assert self.d_current > 0
        for agent in self.agents:
            demand_current += agent(p, self.d_current)
        self.demand_history.append(demand_current)
        self.demand = demand_current
