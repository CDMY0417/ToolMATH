def convert_to_power_of_two(number: float) -> str:
    from math import log2
    return f'2^{{{log2(number)}}}'
