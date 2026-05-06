def calculate_number_of_blocks(target_volume: float, block_volume: float) -> int:
    import math
    return math.ceil(target_volume / block_volume)
