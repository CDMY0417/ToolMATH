def modular_congruence_solution(a: int, b: int, m: int) -> int:
    remainder = (b - a) % m
    if remainder < 0:
        remainder += m
    return remainder
