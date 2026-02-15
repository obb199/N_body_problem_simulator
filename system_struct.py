from utils import compute_distance
import matplotlib.pyplot as plt
import numpy as np


class System:
    def __init__(self, bodies, full_mass_center_hist=False):
        self.full_mass_center_hist = full_mass_center_hist
        self.bodies = bodies
        self.total_mass = sum([b.mass for b in bodies])
        self.kinematic_energy_hist = []
        self.gravitational_energy_hist = []
        self.linear_momentum_hist = []
        self.rotational_momentum_hist = []
        self.mass_center_hist = []

    def mass_center_computation(self):
        mass_center_x = sum(b.mass*b.position[0] for b in self.bodies)/self.total_mass
        mass_center_y = sum(b.mass*b.position[1] for b in self.bodies)/self.total_mass

        mass_center = np.array([mass_center_x, mass_center_y])
        self.mass_center_hist.append(mass_center)

        if len(self.mass_center_hist) >= 3 and not self.full_mass_center_hist:
            self.mass_center_hist.pop(0)

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

    def linear_momentum_computation(self, computation_relativity_to_center_mass=None, dt=None):
        system_linear_momentum = [0, 0]
        for body in self.bodies:
            body_linear_momentum = body.linear_momentum
            system_linear_momentum[0] += body_linear_momentum[0]
            system_linear_momentum[1] += body_linear_momentum[1]

        if computation_relativity_to_center_mass is not None and dt is not None and len(self.mass_center_hist) >= 2:
            cm_velocity_x = (self.mass_center_hist[1][0] - self.mass_center_hist[0][0]) / dt
            cm_velocity_y = (self.mass_center_hist[1][1] - self.mass_center_hist[0][1]) / dt
            system_linear_momentum[0] -= self.total_mass * cm_velocity_x
            system_linear_momentum[1] -= self.total_mass * cm_velocity_y
            resultant_linear_momentum = np.linalg.norm(system_linear_momentum)
            self.linear_momentum_hist.append(float(resultant_linear_momentum))

        resultant_linear_momentum = np.linalg.norm(system_linear_momentum)
        self.linear_momentum_hist.append(float(resultant_linear_momentum))

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
        initial_energy = self.gravitational_energy_hist[0] + self.kinematic_energy_hist[0]
        total_energy = np.array(self.kinematic_energy_hist) + np.array(self.gravitational_energy_hist)
        error_energy = np.abs((total_energy - initial_energy) / initial_energy)
        plt.plot(error_energy)
        plt.xlabel('Iteration')
        plt.ylabel('Energies diff abs(E - E0 / E0)')
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
