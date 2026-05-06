def prob_random_gt_sum_two_distinct(m: int, n: int):
    # Probability that random integer from 1..n is greater than sum of two distinct from 1..m
    pairs = 0
    favorable = 0
    for i in range(1, m+1):
        for j in range(i+1, m+1):
            s = i + j
            pairs += 1
            favorable += max(0, n - s)
    return favorable / (pairs * n)
