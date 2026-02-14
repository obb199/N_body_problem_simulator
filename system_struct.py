from utils import compute_distance
import matplotlib.pyplot as plt
import numpy as np


class System:
    def __init__(self, bodies):
        self.bodies = bodies
        self.kinematic_energy_hist = []
        self.gravitational_energy_hist = []
        self.linear_momentum_hist = []
        self.rotational_momentum_hist = []

    def kinematic_energy_computation(self):
        kinematic_energy = 0
        for body in self.bodies:
            kinematic_energy += body.kinematic_energy

        self.kinematic_energy_hist.append(kinematic_energy)

    def gravitational_energy_computation(self, G):
        gravitational_energy = 0

        n = len(self.bodies)
        for i in range(n):
            for j in range(i+1, n):
                _, _, distance = compute_distance(self.bodies[i].position, self.bodies[j].position)
                gravitational_energy -= G * self.bodies[i].mass * self.bodies[j].mass / distance

        self.gravitational_energy_hist.append(gravitational_energy)

    def linear_momentum_computation(self):
        linear_momentum = 0
        for body in self.bodies:
            linear_momentum += body.linear_momentum

        self.linear_momentum_hist.append(float(linear_momentum))

    def rotational_momentum_computation(self):
        rotational_momentum = 0
        for body in self.bodies:
            rotational_momentum += body.rotational_momentum

        self.rotational_momentum_hist.append(float(rotational_momentum))

    def plot_kinematic_energy_history(self):
        plt.plot(self.kinematic_energy_hist)
        plt.xlabel('Iteration')
        plt.ylabel('Kinematic Energy')
        plt.title('Kinematic Energy over simulation')
        plt.show()

    def plot_gravitational_energy_history(self):
        plt.plot(self.gravitational_energy_hist)
        plt.xlabel('Iteration')
        plt.ylabel('Gravitational Energy')
        plt.title('Gravitational Energy over simulation')
        plt.show()

    def plot_total_energy_history(self):
        total_energy = np.array(self.kinematic_energy_hist) + np.array(self.gravitational_energy_hist)
        plt.plot(total_energy)
        plt.xlabel('Iteration')
        plt.ylabel('Total Energy')
        plt.title('Total Energy over simulation')
        plt.show()

    def plot_energy_comparison(self):
        total_energy = np.array(self.kinematic_energy_hist) + np.array(self.gravitational_energy_hist)
        plt.plot(self.kinematic_energy_hist, label='Kinematic Energy')
        plt.plot(self.gravitational_energy_hist, label='Gravitational Energy')
        plt.plot(total_energy, label='Total Energy')
        plt.legend()
        plt.xlabel('Iteration')
        plt.ylabel('Energies')
        plt.title('Energies over simulation')
        plt.show()

    def plot_energy_error_history(self):
        diff_energy = np.array(self.kinematic_energy_hist) - np.array(self.gravitational_energy_hist)
        plt.plot(diff_energy)
        plt.xlabel('Iteration')
        plt.ylabel('Energies diff (K-U)')
        plt.title('Energy error over simulation')
        plt.show()

    def plot_linear_momentum_history(self):
        plt.plot(self.linear_momentum_hist)
        plt.xlabel('Iteration')
        plt.ylabel('Linear Momentum Module')
        plt.title('Linear Momentum Module over simulation')
        plt.show()

    def plot_rotational_momentum_history(self):
        plt.plot(self.rotational_momentum_hist)
        plt.xlabel('Iteration')
        plt.ylabel('Rotational Momentum Module')
        plt.title('Rotational Momentum Module over simulation')
        plt.show()
