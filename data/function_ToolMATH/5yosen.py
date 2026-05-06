def solve_interval_inequality(A: int, B: int):
    if A > B:
        return []
    return list(range(A, B + 1))
