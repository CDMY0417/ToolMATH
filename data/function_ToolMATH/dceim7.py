def count_outfit_combinations(shirts: int, pants: int, ties: int) -> int:
    tie_options = ties + 1
    return shirts * pants * tie_options
