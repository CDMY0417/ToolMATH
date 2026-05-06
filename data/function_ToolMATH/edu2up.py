def power_inequality_solution(base_a: int, base_b: int) -> int:
    n = 1
    while (base_a ** (n + 1)) >= (base_b ** n):
        n += 1
    return n
