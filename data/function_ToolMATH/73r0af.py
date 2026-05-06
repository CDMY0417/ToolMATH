def factor_integer_out(c: int, expression: str) -> tuple[int, str]:
    terms = expression.split('-') if '-' in expression else expression.split('+')
    terms = [t.strip() for t in terms]
    terms = [f"{c}*({t})" if t != '' else '' for t in terms]
    return c, ' + '.join(terms) if '-' not in expression else ' - '.join(terms)
