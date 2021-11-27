import matplotlib.pyplot as plt

from market import Market
from agent.rational import RationalAgent

market = Market(2.0)


for i in range(10):
    market.add_agent(RationalAgent())

for i in range(100):
    market.simulate()

plt.grid()
plt.plot(market.demand_history[2:]) # The initial price is too big, so we need to cut stabilization
plt.show()
