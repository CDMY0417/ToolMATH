def smallest_solution(a: float, b: float, c: float, d: float) -> float:
    solutions = [a, -a, b, -b, c, -c, d, -d]
    return min(solutions)
