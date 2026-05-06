def minimum_tiles_needed(floor_area: float, tile_area: float) -> int:
    import math
    return math.ceil(floor_area / tile_area)
