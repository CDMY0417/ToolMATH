def sum_of_repeated_block_digits(block: str, repeats: int) -> int:
    sum_of_digits = sum(int(digit) for digit in block)
    return repeats * sum_of_digits
