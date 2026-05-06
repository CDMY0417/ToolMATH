def solve_congruence_for_value(k: int, n: int, m: int) -> int:
    for x in range(1, m):
        if (k * x) % m == n % m:
            return x
    return None
