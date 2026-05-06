def has_exactly_one_root(f_at_start: float, f_at_end: float) -> bool:
    return (f_at_start < 0 < f_at_end) or (f_at_end < 0 < f_at_start)
