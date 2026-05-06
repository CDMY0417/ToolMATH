def projection_matrix(cos_theta: float, sin_theta: float):
    return [[cos_theta**2, cos_theta * sin_theta], [cos_theta * sin_theta, sin_theta**2]]
