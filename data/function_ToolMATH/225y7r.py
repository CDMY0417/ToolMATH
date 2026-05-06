def yen_to_usd(yen_amount: float, yen_to_usd_rate: float) -> float:
    return round(yen_amount / yen_to_usd_rate, 2)
