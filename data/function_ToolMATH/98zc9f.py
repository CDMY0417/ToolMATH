def digit_sum_divisibility(a: int, n_digits: int, divisor: int) -> bool:
    return (n_digits * a) % divisor == 0
