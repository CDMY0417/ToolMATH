def solve_linear_equation_as(a: int, b: int, c: int, d: int):
    coefficient = a - c
    constant = d - b
    if coefficient == 0:
        if constant == 0:
            return 'Infinite solutions'
        else:
            return 'No solution'
    return constant / coefficient
