def partitions_of_n(n: int, m: int):
    def partitions(n, I=1):
        if n == 0:
            yield []
        for i in range(I, n + 1):
            for p in partitions(n - i, i):
                yield [i] + p
    return [p for p in partitions(n) if len(p) <= m]
