import numpy as np

def compute_kinematic_energy(bodies, history):
    for idx, b in enumerate(bodies):
        v = b.velocity_x ** 2 + b.velocity_y ** 2
        kinematic_energy = b.mass * v / 2
        history[idx].append(kinematic_energy)