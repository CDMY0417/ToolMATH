def count_subsets_no_consecutive_min_ge_size(n: int):
    """Return count of subsets with no consecutive elements and min >= size."""
    if n <= 0:
        return 0
    count = 0
    for mask in range(1, 1 << n):
        S = [i + 1 for i in range(n) if (mask >> i) & 1]
        if any(S[i+1] == S[i] + 1 for i in range(len(S) - 1)):
            continue
        k = len(S)
        if min(S) < k:
            continue
        count += 1
    return count
