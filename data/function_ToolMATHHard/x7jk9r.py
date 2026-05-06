def add_base_numbers(a_str: str, b_str: str, base: int):
    """Return a+b in given base as string."""
    n = int(a_str, base) + int(b_str, base)
    if n == 0:
        return '0'
    digits = []
    while n > 0:
        digits.append(str(n % base))
        n //= base
    return ''.join(reversed(digits))
