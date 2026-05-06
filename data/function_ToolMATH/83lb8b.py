def count_non_divisible_by_three(upper_limit: int) -> int:
    count = 0
    for n in range(1, upper_limit + 1):
        if n % 3 != 0:
            count += 1
    return count
