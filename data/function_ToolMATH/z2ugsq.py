def calculate_volume_from_factors(factors: dict[int, int]) -> int:
    volume = 1
    for factor, power in factors.items():
        volume *= factor ** (power // 2)
    return volume
