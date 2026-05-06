def difference_of_cubes_from_diff_and_sum_sq(diff: float, sumsq: float):
    """Return a^3-b^3 = diff*(sumsq + ab) with ab=(sumsq-diff^2)/2."""
    ab = (sumsq - diff*diff) / 2.0
    return diff * (sumsq + ab)
