import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from body_struct import Body
from dynamic_computation import *
from energy_computation import *

matplotlib.use("TkAgg")

plt.style.use("dark_background")
G = 1
dt = 0.003
b1 = Body(5000, 0, 0, 0, 0)
b2 = Body(25, 0, 10, 3, 3)
b3 = Body(100, 3, -10, 8, 8)
b4 = Body(5, 8, -5, 4, 1)
bodies = [b1, b3]

for b in bodies:
    b.traj_x = []
    b.traj_y = []

# calcular aceleração inicial
compute_accelerations(bodies, G)

# =============================== # Configuração da figura # ===============================
fig, ax = plt.subplots()
ax.set_xlim(-30, 30)
ax.set_ylim(-30, 30)
ax.set_title("Simulação N-corpos (Gravitação Newtoniana)")

# =============================== # Scatter (corpos) # ===============================
sizes = [np.sqrt(b.mass) * 5 for b in bodies]

initial_positions = np.array([[b.position_x, b.position_y] for b in bodies])
colors = ["yellow", "red", "blue", "green"]
colors = ["yellow", "red"]

scat = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], s=sizes, c=colors)

# =============================== # Linhas das trajetórias # ===============================
lines = []
for i, b in enumerate(bodies):
    line, = ax.plot([], [], lw=1, color=colors[i], alpha=0.7)
    lines.append(line)


# =============================== # Função init() # ===============================
def init():
    scat.set_offsets(initial_positions)
    for line in lines:
        line.set_data([], [])
    return [scat, *lines]


# =============================== # Função update() # ===============================
def update(frame):
    MAX_TRAIL = 500
    # Atualiza física
    update_params_Leapfrog(bodies, G, dt)
    positions = []
    for i, b in enumerate(bodies):
        positions.append([b.position_x, b.position_y])

    # Salvar histórico
    b.traj_x.append(b.position_x)
    b.traj_y.append(b.position_y)

    # Limitar tamanho do rastro

    if len(b.traj_x) > MAX_TRAIL:
        b.traj_x.pop(0)
        b.traj_y.pop(0)

    # Atualizar linha
    lines[i].set_data(b.traj_x, b.traj_y)

    # Atualizar posições dos corpos
    scat.set_offsets(positions)
    return [scat, *lines]


# =============================== # Criar animação # ===============================
ani = FuncAnimation(fig, update, frames=1000, init_func=init, blit=True, interval=1)
plt.show()
