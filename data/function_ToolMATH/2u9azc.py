def expand_numerator(num1: tuple, num2: tuple, common_denom: int) -> str:
    lhs = f'{num1[0]}*({num1[1]})/{common_denom}'
    rhs = f'{num2[0]}*({num2[1]})/{common_denom}'
    return f'({lhs}) + ({rhs})'
