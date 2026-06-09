import numpy as np
temperatures = np.array([60, 70, 80, 90, 100])
A = 8.07131
B = 1730.63
C = 233.426
P_star = 10 ** (A - B/(C + temperatures))
for i in range(len(temperatures)):
    print(f"T={temperatures[i]}°C → P*={P_star[i]:.2f} mmHg")
