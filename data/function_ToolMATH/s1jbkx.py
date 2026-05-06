def count_two_digit_numbers(target_remainder: int) -> int:
    count = 0
    for n in range(10, 100):
        if n % 3 == target_remainder:
            count += 1
    return count
