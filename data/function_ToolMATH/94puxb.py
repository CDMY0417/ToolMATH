def rebase_exponent(base: int, exp: int, new_base: int) -> float:
    import math
    new_exp = exp * (math.log(base) / math.log(new_base))
    return new_exp
