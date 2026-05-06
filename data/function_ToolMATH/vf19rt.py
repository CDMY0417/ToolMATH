def find_scaling_factor(x: float, y: float, h: float, k: float) -> float:
    return (y - k) / ((x - h) ** 2)
