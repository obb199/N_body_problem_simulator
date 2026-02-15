from body_struct import Body
from system_struct import System
from dynamic_computation import *

G = 1
dt = 0.003
b1 = Body(5000, 0, 0, 0, 0)
b2 = Body(25, 0, 10, 3, 3)
b3 = Body(100, 3, -10, 8, 8)
b4 = Body(1500, 8, -5, 4, 1)
bodies = [b1, b3]
system = System(bodies)

for i in range(1000):
    compute_accelerations(bodies, G)
    update_params_Leapfrog(bodies, G, dt)
    system.kinematic_energy_computation()
    system.gravitational_energy_computation(G)
    system.mass_center_computation()
    system.linear_momentum_computation(True, dt)
    system.rotational_momentum_computation()

system.plot_rotational_momentum_history()
system.plot_gravitational_energy_history()
system.plot_kinematic_energy_history()
system.plot_total_energy_history()
system.plot_energy_error_history()
system.plot_energy_comparison()
system.plot_linear_momentum_history()
system.plot_rotational_momentum_history()

