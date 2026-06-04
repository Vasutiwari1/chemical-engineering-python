# =============================================
# Reynolds Number Calculator
# Author: Vasu Tiwari
# College: PDPU — Chemical Engineering
# Year: 2025
# =============================================

def reynolds(rho, v, D, mu):
    Re = (rho * v * D) / mu
    if Re < 2100:
        flow_type = "Laminar flow"
    elif 2100 <= Re <= 4000:
        flow_type = "Transitional flow"
    elif Re > 4000:
        flow_type = "Turbulent flow"
    return Re, flow_type      

print("=== Reynolds Number Calculator ===\n")
rho = float(input("Enter density (kg/m³): "))
v   = float(input("Enter velocity (m/s): "))
D   = float(input("Enter diameter (m): "))
mu  = float(input("Enter viscosity (Pa·s): "))

Re, flow_type = reynolds(rho, v, D, mu)

print(f"\nDensity     = {rho} kg/m³")
print(f"Velocity    = {v} m/s")
print(f"Diameter    = {D} m")
print(f"Viscosity   = {mu} Pa·s")
print(f"Reynolds No = {Re:.2f}")
print(f"Flow Type   = {flow_type}")