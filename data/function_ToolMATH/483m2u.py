def linear_solution_greater_than_or_equal(a: int, b: int, target: int, threshold: int):
    if a == 0:
        return None if b != target else (threshold if threshold >= target else None)
    solution = (target - b) / a
    return solution if solution >= threshold else None
