def expand_binomial_product_h(binomial1: tuple, binomial2: tuple):
    a, b = binomial1
    c, d = binomial2
    return (a*c, a*d + b*c, b*d)
