def sum_odd_even_positions(digits: list[int]) -> int:
    odd_sum = sum(digits[i] for i in range(0, len(digits), 2))
    even_sum = sum(digits[i] for i in range(1, len(digits), 2))
    return odd_sum * 3 + even_sum
