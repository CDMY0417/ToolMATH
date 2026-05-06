def find_integer_in_interval_with_remainder(lo: int, hi: int, remainder: int, modulus: int):
    for n in range(lo, hi + 1):
        if n % modulus == remainder:
            return n
    return None
