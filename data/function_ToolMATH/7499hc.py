def exclude_values_from_domain(excluded_values: list[float]) -> str:
    intervals = []
    values = sorted(excluded_values)
    for i in range(len(values) + 1):
        if i == 0:
            intervals.append(f'(-\infty, {values[i]})')
        elif i == len(values):
            intervals.append(f'({values[i-1]}, \infty)')
        else:
            intervals.append(f'({values[i-1]}, {values[i]})')
    return ' \cup '.join(intervals)
