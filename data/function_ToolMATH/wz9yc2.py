def calculate_tiles_needed_b(area_side_length: int, tile_side_length: int) -> int:
    tiles_per_side = area_side_length // tile_side_length
    return tiles_per_side * tiles_per_side
