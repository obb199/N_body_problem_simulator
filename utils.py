import numpy as np

def compute_distance(d1, d2, epsilon=1e-5):
    distance_x = (d2[0] - d1[0])
    distance_y = (d2[1] - d1[1])
    total_distance = np.linalg.norm([distance_x, distance_y]) + epsilon
    return distance_x, distance_y, total_distance
