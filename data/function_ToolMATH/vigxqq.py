def sin_squared_angle_sequence(a_0: float, n: int) -> float:
    a_n = a_0
    for _ in range(n):
        a_n = 4 * a_n * (1 - a_n)
    return a_n
