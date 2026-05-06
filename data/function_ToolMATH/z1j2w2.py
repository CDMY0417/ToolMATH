def is_multiple_of_three_a(n: int) -> bool:
    return sum(int(digit) for digit in str(n)) % 3 == 0
