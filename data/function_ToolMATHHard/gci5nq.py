def count_three_digit_numbers_with_digit_min_and_divisibility(digit_min: int, divisor: int):
    """Return count of three-digit numbers meeting digit and divisibility constraints."""
    if digit_min < 0 or digit_min > 9:
        raise ValueError("digit_min out of range.")
    if divisor <= 0:
        raise ValueError("divisor must be positive.")
    count = 0
    for n in range(100, 1000):
        s = str(n)
        if all(int(ch) >= digit_min for ch in s) and n % divisor == 0:
            count += 1
    return count
