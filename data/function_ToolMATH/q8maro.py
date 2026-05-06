def is_divisible_by_11_d(number: int) -> bool:
    digits = [int(d) for d in str(number)]
    alt_sum = sum(digits[i] if i % 2 == 0 else -digits[i] for i in range(len(digits)))
    return alt_sum % 11 == 0
