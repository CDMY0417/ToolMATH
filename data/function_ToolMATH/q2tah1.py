def apply_demoivres_theorem_a(r: float, theta: float, n: int):
    import cmath
    r_n = r**n
    theta_n = theta * n
    return r_n, theta_n
