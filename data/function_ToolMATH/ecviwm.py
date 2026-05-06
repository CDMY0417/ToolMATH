def angle_in_specified_range(angle: int, upper_bound: int) -> int:
    equivalent = angle % 360
    return equivalent if equivalent <= upper_bound else equivalent - 360
