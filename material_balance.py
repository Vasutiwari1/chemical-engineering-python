
import numpy as np
A=np.array([[1,1],
            [0.4,0.7]])
B=np.array([100,60])
x=np.linalg.solve(A,B)
y=np.round(x,3)
print(f"F1,F2={y}Kg/hr",)
            