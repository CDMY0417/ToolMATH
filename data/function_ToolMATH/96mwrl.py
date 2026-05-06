def calculate_expression_value(expressions: dict[str, int], values: dict[str, int]) -> int:
    return sum(coefficient * values[var] for var, coefficient in expressions.items())
