def power_of_two_representation(x: float) -> int:
    import math
    return int(math.log2(x)) if x > 0 else None
