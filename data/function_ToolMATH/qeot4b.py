def integer_partitions_with_fixed_length(n: int, k: int):
    if k > n:
        return []
    if k == 1:
        return [(n,)]
    partitions = []
    for i in range(n, 0, -1):
        for subpartition in integer_partitions_with_fixed_length(n-i, k-1):
            if subpartition and i >= subpartition[0]:
                partitions.append((i,) + subpartition)
    return partitions
