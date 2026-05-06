def compute_star_operator_value(a, b, c, d, target, e, f, g, h):
    # Solve for ops in {+,-,*,/} so (a ⋆ b)/(c * d) = target, then compute (e ⋆ f)/(g * h)
    ops = ['+', '-', '*', '/']
    def apply(x, y, op):
        if op == '+':
            return x + y
        if op == '-':
            return x - y
        if op == '*':
            return x * y
        if op == '/':
            if y == 0:
                return None
            return x / y
    for op1 in ops:
        num = apply(a, b, op1)
        if num is None:
            continue
        for op2 in ops:
            den = apply(c, d, op2)
            if den in (None, 0):
                continue
            if abs(num / den - target) < 1e-9:
                num2 = apply(e, f, op1)
                den2 = apply(g, h, op2)
                if den2 in (None, 0):
                    continue
                return num2 / den2
    raise ValueError('no operator pair satisfies the condition')
