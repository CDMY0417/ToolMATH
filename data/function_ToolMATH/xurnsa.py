def smallest_multiple_greater_than_b(divisor: int, min_value: int) -> int:
    quotient = min_value // divisor
    if min_value % divisor == 0:
        return min_value
    else:
        return divisor * (quotient + 1)
