def estimate_population(marked_count: int, observed_count: int, marked_in_observed: int) -> int:
    proportion_marked = marked_in_observed / observed_count
    estimated_total = marked_count / proportion_marked
    return round(estimated_total)
