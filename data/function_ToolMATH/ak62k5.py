def calculate_fill_time(initial_time: float, initial_volume: float, target_volume: float, initial_faucets: int, target_faucets: int):
    time_ratio = initial_faucets / target_faucets
    volume_ratio = target_volume / initial_volume
    return initial_time * volume_ratio * time_ratio
