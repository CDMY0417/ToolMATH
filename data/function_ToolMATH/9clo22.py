def calculate_other_endpoint(x1: int, y1: int, cx: int, cy: int):
    dx = cx - x1
    dy = cy - y1
    return (cx + dx, cy + dy)
