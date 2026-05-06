def integer_partitions(n: int, k: int):
    def _partition_helper(n, k, min_val, current):
        if k == 0:
            if n == 0:
                yield tuple(current)
            return
        for i in range(min_val, n + 1):
            yield from _partition_helper(n - i, k - 1, i, current + [i])
    return list(_partition_helper(n, k, 0, []))
