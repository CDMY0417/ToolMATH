def is_divisor_in_range(n: int, divisor: int, lo: int, hi: int) -> bool:
    return n % divisor == 0 and lo <= divisor <= hi
