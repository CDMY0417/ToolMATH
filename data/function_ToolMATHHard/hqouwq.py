def least_three_digit_with_mod_condition(m: int, threshold: int):
    """Return least three-digit n with n mod m > threshold."""
    for n in range(100, 1000):
        if n % m > threshold:
            return n
    return None
