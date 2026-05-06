def alternate_sum(number: int) -> int:
    digits = [int(d) for d in str(number)]
    return sum(digits[i] if i % 2 == 0 else -digits[i] for i in range(len(digits)))
