def rewrite_base_exponent(base: int, outer_exponent: int, inner_base: int):
    import math
    exponent = outer_exponent * int(math.log(base, inner_base))
    return (inner_base, exponent)
