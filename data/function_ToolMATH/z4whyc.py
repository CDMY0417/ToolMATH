def change_of_base_logarithm(value: float, original_base: int, new_base: int):
    import math
    return value / (math.log(original_base, new_base))
