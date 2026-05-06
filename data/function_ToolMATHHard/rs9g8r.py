def remainder_mod_x2_minus1(coeffs):
    # Remainder r(x)=ax+b when dividing by x^2-1 using f(1), f(-1)
    def eval_poly(x):
        s=0
        for i,c in enumerate(coeffs):
            s += c*(x**i)
        return s
    f1 = eval_poly(1)
    fneg = eval_poly(-1)
    a = (f1 - fneg)/2
    b = (f1 + fneg)/2
    return [a, b]
