def compute_distance(d1, d2, episilon=1e-5):
    distance_x = (d2[0] - d1[0])
    distance_y = (d2[1] - d1[1])
    total_distance = (distance_x ** 2 + distance_y ** 2) ** 0.5 + episilon
    return distance_x, distance_y, total_distance