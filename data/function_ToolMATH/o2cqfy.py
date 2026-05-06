def probability_of_digit_in_repeating_block(repeating_block: str, target_digit: str) -> float:
    count = repeating_block.count(target_digit)
    total_digits = len(repeating_block)
    return count / total_digits if total_digits > 0 else 0
