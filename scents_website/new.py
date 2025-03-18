import numpy as np
import matplotlib.pyplot as plt

# Define quantity range
quantity = np.linspace(0, 100, 100)

# Define demand and supply functions
def demand(q):
    return 200 - 2 * q  # Downward sloping demand curve

def supply(q):
    return 50 + 1.5 * q  # Upward sloping supply curve

def world_supply(q):
    return 80  # World price level

def world_supply_tariff(q):
    return 100  # World price with tariff

# Generate price data
price_demand = demand(quantity)
price_supply = supply(quantity)
world_price = world_supply(quantity)
world_price_tariff = world_supply_tariff(quantity)

# Plot the curves
plt.figure(figsize=(10, 6))
plt.plot(quantity, price_demand, label='Demand (Dd)', color='blue')
plt.plot(quantity, price_supply, label='Domestic Supply (Sd)', color='green')
plt.axhline(y=80, color='purple', linestyle='--', label='World Price (Pw)')
plt.axhline(y=100, color='red', linestyle='--', label='World Price with Tariff (Pt)')

# Label equilibrium points
plt.scatter([40], [demand(40)], color='black', zorder=3)  # Equilibrium without tariff
plt.text(42, demand(40), 'E1', fontsize=12)
plt.scatter([30], [demand(30)], color='black', zorder=3)  # Equilibrium with tariff
plt.text(32, demand(30), 'E2', fontsize=12)

# Labels and title
plt.xlabel("Quantity of Aluminium")
plt.ylabel("Price of Aluminium ($)")
plt.title("Impact of Tariffs on Aluminium Market")
plt.legend()
plt.grid()
plt.show()
