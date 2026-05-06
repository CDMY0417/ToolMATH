def substitute_variable_d(eq1: str, eq2: str, expr_for_substitution: str, variable_to_replace: str):
    eq2 = eq2.replace(variable_to_replace, expr_for_substitution)
    return eq2
