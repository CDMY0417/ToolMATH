def solve_linear_inequality_e(a: float, b: float, c: float) -> str:
    if a == 0:
        return 'No solution' if b > c else 'All x satisfy the inequality' if b <= c else 'x could be anything'
    solution = (c - b) / a
    if a > 0:
        return f'x <= {solution}'
    else:
        return f'x >= {solution}'
