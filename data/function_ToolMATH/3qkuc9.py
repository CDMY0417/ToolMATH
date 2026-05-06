def substitute_parameters(x_expr: str, y_expr: str, z_expr: str, c: str, d: str) -> str:
    x_sub = f'({x_expr})'
    y_sub = f'({y_expr})'
    z_sub = f'({z_expr})'
    return f'{x_sub} + {y_sub} + {c}*{z_sub} - {d}'
