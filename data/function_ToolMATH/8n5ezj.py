def solve_linear_equations_a(sum_eq: int, diff_eq: int) -> tuple:
    a = (sum_eq + diff_eq) // 2
    b = (sum_eq - diff_eq) // 2
    return a, b
