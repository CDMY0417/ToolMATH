def linear_diophantine_solution(a: int, b: int) -> tuple:
    x0, y0, a0, b0 = 1, 0, a, b
    x1, y1 = 0, 1
    while b0:
        q = a0 // b0
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
        a0, b0 = b0, a0 % b0
    return x0, y0
