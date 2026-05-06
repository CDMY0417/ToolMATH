def total_coin_value(count: int, denominations: list[float]) -> float:
    return sum(d * count for d in denominations)
