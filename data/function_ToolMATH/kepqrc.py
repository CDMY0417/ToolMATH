def translate_segment(segment: tuple, direction: str, distance: int):
    if direction == 'vertical':
        return (segment[0], segment[1] + distance)
    elif direction == 'horizontal':
        return (segment[0] + distance, segment[1])
    return segment
