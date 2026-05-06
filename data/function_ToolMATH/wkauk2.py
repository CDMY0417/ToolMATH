def substitute_variable_f(eq_main: str, eq_substitute: str, variable: str):
    substitute_expr = eq_substitute.split('=')[1].strip()
    eq_main = eq_main.replace(variable, substitute_expr)
    return eq_main
