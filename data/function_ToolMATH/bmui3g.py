def solve_linear_system_a(sum_val: int, diff_val: int) -> tuple:
    a = (sum_val + diff_val) // 2
    c = (sum_val - diff_val) // 2
    return a, c
