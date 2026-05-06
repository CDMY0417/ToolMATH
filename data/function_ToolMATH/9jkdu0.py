def count_total_orderings(base_orderings: int, positions_per_insertion: list[int]) -> int:
    total_orderings = base_orderings
    for positions in positions_per_insertion:
        total_orderings *= positions
    return total_orderings
