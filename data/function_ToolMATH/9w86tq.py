def solve_congruence_a(a: int, b: int, m: int):
    solutions = []
    for x in range(m):
        if (a * x) % m == b % m:
            solutions.append(x)
    return solutions
