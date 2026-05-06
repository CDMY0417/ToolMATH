def modular_arithmetic_solution(a1: int, m1: int, a2: int, m2: int) -> int:
    solution = a1
    while solution % m2 != a2 % m2:
        solution += m1
    return solution
