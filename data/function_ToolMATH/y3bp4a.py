def integer_partitions_with_fixed_bins(total: int, bins: int):
    def partitions(n, k, min_val, prefix):
        if k == 1:
            yield prefix + (n,)
        else:
            for i in range(min_val, n // k + 1):
                yield from partitions(n - i, k - 1, i, prefix + (i,))
    
    return list(partitions(total, bins, 0, ()))
