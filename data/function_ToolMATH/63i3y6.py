def clock_equivalent(time1: int, time2: int) -> bool:
    return (time1 - time2) % 12 == 0
