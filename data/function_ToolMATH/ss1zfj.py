def count_odd_multiples_in_range(multiple: int, start: int, end: int) -> int:
    count = 0
    for i in range(start + (start % 2 == 0), end, 2):
        if i % multiple == 0:
            count += 1
    return count
