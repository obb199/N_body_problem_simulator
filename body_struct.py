import numpy as np
from utils import distance_computation


class Body:
    def __init__(self, mass: float,
                 pos_x: float = 0, pos_y: float = 0,
                 vel_x: float = 0, vel_y: float = 0):

        self.mass = mass
        self.position_x = pos_x
        self.position_y = pos_y
        self.velocity_x = vel_x
        self.velocity_y = vel_y
        self.acceleration_x = 0
        self.acceleration_y = 0
        self.force_x = 0
        self.force_y = 0
        self.kinematic_energy = mass * (vel_x**2 + vel_y**2) / 2
        self.linear_momentum = mass * (vel_x**2 + vel_y**2) ** 0.5
        self.rotational_momentum = m * (pos_x**2 + pos_y**2) ** 0.5 * (vel_x**2 + vel_y**2) ** 0.5

    @property
    def position(self):
        return np.array([self.position_x,
                         self.position_y])
