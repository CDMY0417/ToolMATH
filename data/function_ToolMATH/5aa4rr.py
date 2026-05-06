def multiply_both_sides_c(lhs: str, rhs: str, expression: str) -> tuple:
    new_lhs = f'({lhs}) * ({expression})'
    new_rhs = f'({rhs}) * ({expression})'
    return new_lhs, new_rhs
