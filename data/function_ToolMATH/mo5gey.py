def sum_square_roots(expressions: list[int], integer: int) -> str:
    result = ' + '.join([f'sqrt({x})' for x in expressions])
    return f'{result} - {integer}'
