def sum_of_cycle_contributions(cycle: list[int], term_count: int) -> int:
    cycle_length = len(cycle)
    full_cycles = term_count // cycle_length
    remaining_terms = term_count % cycle_length
    cycle_sum = sum(cycle)
    total = full_cycles * cycle_sum
    total += sum(cycle[:remaining_terms])
    return total
