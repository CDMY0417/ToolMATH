def remove_parentheses(expression: str) -> str:
    import re
    expression_no_parentheses = re.sub(r'\(([^\(\)]+)\)', r'\1', expression)
    return expression_no_parentheses
