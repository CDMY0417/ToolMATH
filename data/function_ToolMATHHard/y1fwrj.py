def sum_distinct_sums_three_draws(values):
    # Sum of all distinct sums from three draws with replacement
    sums=set()
    for a in values:
        for b in values:
            for c in values:
                sums.add(a+b+c)
    return sum(sums)
