def apply_demoivres_theorem(theta: float, n: int) -> float:
    theta_n = theta * n
    return theta_n % 360
