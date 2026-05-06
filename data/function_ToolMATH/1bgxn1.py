def count_numbers_with_digit(lo: int, hi: int, digit: int, position: str) -> int:
    count = 0
    for number in range(lo, hi + 1):
        if position == 'tens' and (number // 10) % 10 == digit:
            count += 1
        elif position == 'units' and number % 10 == digit:
            count += 1
    return count
