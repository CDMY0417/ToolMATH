def smallest_int_congruent(start: int, modulus: int, target_remainder: int) -> int:
    remainder = start % modulus
    if remainder == target_remainder:
        return start
    elif remainder < target_remainder:
        return start + (target_remainder - remainder)
    else:
        return start + (modulus - remainder) + target_remainder
