def substitute_and_solve(coeff_x: int, coeff_y: int, constant: int, value_x: float) -> float:
    remaining = constant - coeff_x * value_x
    return remaining / coeff_y
