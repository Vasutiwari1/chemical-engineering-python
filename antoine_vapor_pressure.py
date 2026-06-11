import matplotlib.pyplot as plt
import numpy as np
temperatures = np.array([60, 70, 80, 90, 100])
A = 8.07131
B = 1730.63
C = 233.426
P_star = 10 ** (A - B/(C + temperatures))
plt.plot(temperatures,P_star,
         color='red',
         marker='s',
         )
plt.xlabel("TEMPRATURE")
plt.ylabel("WATER VAPOUR PRESSURE")
plt.title("Antoine Equation — Water Vapor Pressure")
plt.grid(True)  
plt.savefig('antoine_graph.png')
plt.show()

