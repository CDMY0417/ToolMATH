def largest_integer_less_than_log_base(number: int, base: int) -> int:
    import math
    log_value = math.log(number, base)
    return int(log_value)
