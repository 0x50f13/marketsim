from market import Market
from agent.rational import RationalAgent

market = Market(0.0)


for i in range(10):
    market.add_agent(RationalAgent())

for i in range(10):
    market.simulate()
