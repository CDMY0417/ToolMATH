def count_isosceles_from_lengths(lengths):
    # Count triangles with exactly two equal sides from given lengths
    count = 0
    for s in lengths:
        for t in lengths:
            if t == s:
                continue
            if 2*s > t:
                count += 1
    return count
