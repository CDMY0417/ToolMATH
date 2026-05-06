def convert_base_10_to_base_n_a(num: int, base: int) -> str:
    if num == 0:
        return '0'
    digits = []
    while num:
        digits.append(int(num % base))
        num //= base
    return ''.join(str(x) for x in digits[::-1])
