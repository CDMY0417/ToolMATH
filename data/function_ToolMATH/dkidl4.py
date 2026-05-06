def substitute_variable_c(expr: str, sub_var: str, sub_expr: str):
    return expr.replace(sub_var, '(' + sub_expr + ')')
