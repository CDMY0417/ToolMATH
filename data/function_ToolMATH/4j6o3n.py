def solve_linear_congruence_c(a: int, b: int, n: int):
    a = a % n
    b = b % n
    for x in range(n):
        if (a * x) % n == b:
            return x
    return None
