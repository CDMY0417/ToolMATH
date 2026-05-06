def solve_linear_equation_fo(a: int, b: int, c: int) -> int:
    # ax + b = c -> ax = c - b -> x = (c - b) / a
    return (c - b) // a
