def evaluate_expression_in_terms_of_variable(expr: str, target_variable: str, value_sum: int):
    variables = {target_variable: 0}
    for var in expr.split('+'):
        coefficients = var.replace(target_variable, '').strip()
        coef_value = int(coefficients) if coefficients else 1
        variables[target_variable] += coef_value
    solved_value = value_sum / variables[target_variable]
    return solved_value
