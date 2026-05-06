def integer_partitions_with_limit(n: int, max_parts: int):
    def generate_partitions(n, max_val, max_parts, prefix=[]):
        if n == 0 and len(prefix) <= max_parts:
            yield prefix
        for i in range(min(n, max_val), 0, -1):
            if len(prefix) >= max_parts:
                continue
            yield from generate_partitions(n - i, i, max_parts, prefix + [i])

    return list(generate_partitions(n, n, max_parts))
