def sum_multiple_base_numbers(values, base: int):
    """Return sum in given base as string."""
    total = 0
    for v in values:
        total += int(v, base)
    if total == 0:
        return '0'
    digits = []
    while total > 0:
        digits.append(str(total % base))
        total //= base
    return ''.join(reversed(digits))
