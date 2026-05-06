def sum_of_periodic_sequence_terms(start_index: int, num_terms: int, cycle: list[int]) -> int:
    period = len(cycle)
    total_sum = 0
    for i in range(num_terms):
        total_sum += cycle[(start_index + i) % period]
    return total_sum
