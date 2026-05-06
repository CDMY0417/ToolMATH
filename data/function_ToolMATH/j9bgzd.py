def number_of_sections_needed(total_area: float, section_area: float) -> int:
    import math
    return math.ceil(total_area / section_area)
