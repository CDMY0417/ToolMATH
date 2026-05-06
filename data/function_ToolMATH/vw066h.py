def power_base_conversion(base: int, exponent: float, target_base: int):
    import math
    converted_exponent = exponent * math.log(base, target_base)
    return target_base, converted_exponent
