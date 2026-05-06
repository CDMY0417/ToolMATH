def solve_linear_congruence(a: int, b: int, m: int) -> int:
    for x in range(m):
        if (a * x % m) == b % m:
            return x
    return None
