def absolute_value_equation_solutions(a: int, b: int, c: int, d: int):
    solutions = set()
    # Case 1: a*x + b = c*x + d
    if a != c:
        x1 = (d - b) / (a - c)
        if x1 % 1 == 0:  # Check if x1 is an integer
            solutions.add(int(x1))
    # Case 2: a*x + b = -(c*x + d)
    if a != -c:
        x2 = (-b - d) / (a + c)
        if x2 % 1 == 0:  # Check if x2 is an integer
            solutions.add(int(x2))
    return solutions
