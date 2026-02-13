import numpy as np


def compute_kinematic_energy(bodies):
    for idx, b in enumerate(bodies):
        v = b.velocity_x ** 2 + b.velocity_y ** 2
        bodies.kinematic_energy = b.mass * v / 2


def compute_system_kinematic_energy(bodies, history):
    pass


def compute_system_gravitational_energy(bodies, history):
    pass