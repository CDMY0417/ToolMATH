def count_congruent_numbers(a: int, k: int, limit: int) -> int:
    count = 0
    for n in range(1, limit):
        if n % k == a:
            count += 1
    return count
