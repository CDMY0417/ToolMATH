def count_multiples_in_range_d(multiple: int, lo: int, hi: int) -> int:
    start = (lo + multiple - 1) // multiple  # Round up to the nearest multiple
    end = hi // multiple
    return max(0, end - start + 1)
