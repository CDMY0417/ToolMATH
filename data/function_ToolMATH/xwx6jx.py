def calculate_odd_even_combinations(length: int, start_with_odd: bool) -> int:
    odd_count, even_count = 3, 2
    total_combinations = 1
    for i in range(length):
        if (i % 2 == 0 and start_with_odd) or (i % 2 == 1 and not start_with_odd):
            total_combinations *= odd_count
        else:
            total_combinations *= even_count
    return total_combinations
