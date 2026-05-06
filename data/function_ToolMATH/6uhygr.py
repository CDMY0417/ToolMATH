def sign_of_linear_expression(a: int, b: int, x: float) -> str:
    if a * x + b > 0:
        return '+'
    elif a * x + b < 0:
        return '-'
    else:
        return '0'
