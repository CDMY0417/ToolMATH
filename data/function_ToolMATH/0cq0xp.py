def compose_quadratic_n_times(a: float, b: float, c: float, x: float, n: int):
    fx = x
    for _ in range(n):
        fx = a*fx**2 + b*fx + c
    return fx
