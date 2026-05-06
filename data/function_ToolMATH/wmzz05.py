def equally_distribute_volume(total_volume: float, n: int) -> float:
    single_volume = total_volume / n
    r = (single_volume * 1.5 / 3.141592653589793)**(1/3)
    return r
