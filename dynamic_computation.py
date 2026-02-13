import numpy as np
from utils import compute_distance


def compute_force(m1: float, m2: float,
                  p1: list[float], p2: list[float],
                  G: float) -> Tuple[float]:
    """
    Function equation explanation:
        Gravitational Force = G * m1 * m2 * |d| / d³
        G = Gravitational constant (6.6743 * 10⁻¹¹)
        m1 = mass of first body
        m2 = mass of second body
        d = distance of bodies

    Arguments:
        p1: position of first body
        p2: position of second body
    """

    distance_x, distance_y, total_distance = compute_distance(p1, p2)
    common_prod = G * m1 * m2 / (total_distance ** 3)
    force_x = common_prod * distance_x
    force_y = common_prod * distance_y

    return force_x, force_y


def compute_accelerations(bodies: list[object], G: float) -> None:
    """
    Arguments:
        bodies: list of Body class
        G: gravitational constant
    """
    # Forces initialization
    for b in bodies:
        b.force_x = 0
        b.force_y = 0

    # Forces computation
    for b1 in bodies:
        for b2 in bodies:
            if b1 != b2:
                fx, fy = compute_force(b1.mass, b2.mass, b1.position, b2.position, G)
                b1.force_x += fx
                b1.force_y += fy

    #  acceleration convertion
    for b in bodies:
        b.acceleration_x = b.force_x / b.mass
        b.acceleration_y = b.force_y / b.mass


def update_params_euler(bodies: list[object], dt: float) -> None:
    """
    Using acceleration to compute velocity and position
    with euler integration

    Arguments:
        bodies: list of Body class
        dt: time value
    """
    for b in bodies:
        b.velocity_x += b.acceleration_x * dt
        b.position_x += b.velocity_x * dt
        b.velocity_y += b.acceleration_y * dt
        b.position_y += b.velocity_y * dt


def update_params_Leapfrog(bodies: list[object], G: float, dt: float) -> None:
    """
        Arguments:
            bodies: list of Body class
            G: gravitational constant
            dt: time value

        Using acceleration to compute velocity and position with Leapfrog integration:
        Leapprof equations:

            v(t+0.5dt) = v(t) + 0.5*a(t)dt
            x(t+dt) = x(t) + v(t+0.5dt)dt
            v(t+dt) = v(t+0.5dt) + 0.5*a(t+dt)dt
    """

    # first velocity pass half
    for b in bodies:
        b.velocity_x += 0.5 * b.acceleration_x * dt
        b.velocity_y += 0.5 * b.acceleration_y * dt

    # full position pass
    for b in bodies:
        b.position_x += b.velocity_x * dt
        b.position_y += b.velocity_y * dt

    # recompute acceleration
    compute_accelerations(bodies, G)

    # second velocity pass half
    for b in bodies:
        b.velocity_x += 0.5 * b.acceleration_x * dt
        b.velocity_y += 0.5 * b.acceleration_y * dt
