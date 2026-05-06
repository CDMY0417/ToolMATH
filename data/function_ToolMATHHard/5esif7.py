def total_distance_until_nth_hit(h: float, r: float, n: int):
    # Total distance traveled by a bouncing ball until it hits the ground n-th time
    if n < 1:
        return 0.0
    total = h
    # add up-and-down for bounces 2..n
    for i in range(1, n):
        total += 2*h*(r**i)
    return total
