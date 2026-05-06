def nth_digit_in_repeating_block(n: int, block: list[int]) -> int:
    length = len(block)
    position = (n - 1) % length  # Zero-based index
    return block[position]
