def expand_expression_a(expression: str, coefficient: int):
    terms = expression.split('+')
    expanded_terms = [f'{coefficient}*{term}' for term in terms]
    return ' + '.join(expanded_terms)
