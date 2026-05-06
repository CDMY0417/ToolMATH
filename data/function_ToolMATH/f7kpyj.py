def sum_equations(equation1: tuple, equation2: tuple):
    lhs1, rhs1 = equation1
    lhs2, rhs2 = equation2
    new_lhs = f'{lhs1} + {lhs2}'
    new_rhs = f'{rhs1} + {rhs2}'
    return new_lhs, new_rhs
