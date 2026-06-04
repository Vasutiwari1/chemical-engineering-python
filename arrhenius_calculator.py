"""Write a function called arrhenius(A, Ea, T)
Formula: k = A × e^(-Ea/RT)
R = 8.314
Use import math → math.exp()
Return rate constant k

Then use a for loop outside to print k
at T = 300, 400, 500, 600K
Use A = 1e10, Ea = 50000"""
import math
R=8.314
def arrhenius(A,Ea,T):
    import math
    y=(-Ea)/(R*T)
    K =A*math.exp(y)
    return K
A=float(input("Enter pre-exponential factor (A):"))
Ea=float(input("Enter activation energy Ea (J/mol:)"))
T=float(input("ENTER THE TEMPRATURE IN KELVIN:"))
result=arrhenius(A,Ea,T)

print(f"TEMPRATURE={T}K,RATE CONSTANT={result:.3f},ACTIVATION ENERGY={Ea}J/mol,PRE EXPONENTIAL FACTOR={A}")


    
