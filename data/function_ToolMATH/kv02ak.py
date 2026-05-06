def find_critical_points(a: int, b: int, c: int):
    delta = b**2 - 4*a*c
    if delta < 0:
        return []
    sqrt_delta = delta**0.5
    x1 = (-b + sqrt_delta) / (2*a)
    x2 = (-b - sqrt_delta) / (2*a)
    return [x1, x2]
