def find_smallest_integer_sum_at_least(start: int, threshold: int) -> int:
    n = start
    current_sum = 0
    while current_sum < threshold:
        current_sum += n
        n += 1
    return n - 1
