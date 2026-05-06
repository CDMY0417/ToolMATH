def exponential_to_power_of_i(r: float, theta_degrees: float, n: int) -> complex:
    import cmath
    theta_radians = cmath.pi * theta_degrees / 180
    result_r = r ** n
    result_theta_radians = theta_radians * n
    return cmath.rect(result_r, result_theta_radians)
