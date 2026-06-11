import matplotlib.pyplot as plt
import numpy as np

n = 2
R = 8.314
V = 0.05
temperatures = np.array([300, 350, 400, 450, 500])
P = (n * R * temperatures) / V

plt.plot(temperatures, P, color='red', marker='o')
plt.xlabel("Temperature (K)")
plt.ylabel("Pressure (Pa)")
plt.title("Pressure vs Temperature — Ideal Gas")
plt.grid(True)
plt.savefig('pressure_vs_temperature.png')   
plt.show()                                    