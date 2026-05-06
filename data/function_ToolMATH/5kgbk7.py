def evaluate_expression(expression: tuple):
    op1, operator, op2 = expression
    if operator == '+':
        return op1 + op2
    elif operator == '-':
        return op1 - op2
    elif operator == '*':
        return op1 * op2
    elif operator == '/':
        return op1 / op2
    return None
