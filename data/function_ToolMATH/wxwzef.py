def solve_linear(b: int, c: int) -> tuple:
    # Solving (x - b)^2 = c
    root = c ** 0.5
    return (b + root, b - root)
