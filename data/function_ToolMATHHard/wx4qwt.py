def divide_base_numbers(a_str: str, b_str: str, base: int):
    """Return quotient in given base as string (integer division)."""
    n = int(a_str, base)
    d = int(b_str, base)
    q = n // d
    if q == 0:
        return '0'
    digits = []
    while q > 0:
        digits.append(str(q % base))
        q //= base
    return ''.join(reversed(digits))
