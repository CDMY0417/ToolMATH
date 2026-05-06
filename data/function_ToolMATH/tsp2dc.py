def least_multiple_over_threshold(divisor: int, threshold: int) -> int:
    quotient = threshold // divisor
    return (quotient + 1) * divisor
