def multiply_binomials(binomial1: tuple, binomial2: tuple):
    (a, b), (c, d) = binomial1, binomial2
    return (a*c, a*d + b*c, b*d)
