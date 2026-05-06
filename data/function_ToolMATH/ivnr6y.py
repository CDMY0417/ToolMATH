def simplify_expression(expression: str) -> str:
    import re
    terms = re.findall(r'[+-]?\d*x?|\d+', expression)
    coeff_sum = 0
    const_sum = 0
    for term in terms:
        if 'x' in term:
            if term == 'x':
                coeff_sum += 1
            elif term == '-x':
                coeff_sum -= 1
            else:
                coeff_sum += int(term[:-1])
        else:
            const_sum += int(term)
    simplified = f'{coeff_sum}x' if coeff_sum != 0 else ''
    if const_sum > 0:
        simplified += f' + {const_sum}'
    elif const_sum < 0:
        simplified += f' - {-const_sum}'
    return simplified
