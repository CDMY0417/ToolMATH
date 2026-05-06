def factor_common_expression(expression1: str, expression2: str, common_subexpression: str):
    if expression1.endswith(common_subexpression) and expression2.endswith(common_subexpression):
        e1 = expression1[:-len(common_subexpression)].strip()
        e2 = expression2[:-len(common_subexpression)].strip()
        return f'({e1}+{e2}){common_subexpression}'
    return None
