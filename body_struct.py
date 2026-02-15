import numpy as np
from utils import compute_distance


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

    @property
    def position(self):
        return np.array([self.position_x,
                         self.position_y])

    @property
    def kinematic_energy(self):
        return self.mass * (self.velocity_x**2 + self.velocity_y**2) / 2

    @property
    def linear_momentum(self):
        return np.array([
            self.mass * self.velocity_x,
            self.mass * self.velocity_y
        ])

    @property
    def rotational_momentum(self):
        return self.mass * (self.position_x * self.velocity_y - self.position_y * self.velocity_x)

    def dict_infos(self):
        infos = {'mass': self.mass,
                 'position': (self.position_x, self.position_y),
                 'velocity': (self.velocity_x, self.velocity_y),
                 'acceleration': (self.acceleration_x, self.acceleration_y),
                 'force': (self.force_x, self.force_y)}

        return infos


