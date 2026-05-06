def trig_substitute_tan(expression: str) -> str:
    return expression.replace('tan x', 'sin x/cos x')
