import matplotlib.pyplot as plt

from marketsim.market import Market
from marketsim.agent.rational import RationalAgent
from marketsim.agent.anchoring import AnchoringAgent

market = Market(2.0)


#for i in range(100):
#    market.add_agent(AnchoringAgent())

for i in range(100):
    market.add_agent(RationalAgent())


for i in range(300):
    market.simulate(i)

plt.grid()
plt.plot(market.demand_history[100:]) # The initial price is too big, so we need to cut stabilization
plt.show()
plt.grid()
plt.plot(market.price_history[100:])
plt.show()
