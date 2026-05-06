def distance_from_origin_to_plane(alpha: float, beta: float, gamma: float) -> float:
    return 1 / ((1/alpha**2 + 1/beta**2 + 1/gamma**2) ** 0.5)
