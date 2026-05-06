def scale_open_interval(low: float, high: float, scale: float):
    """Return (low/scale, high/scale) for scale>0."""
    if scale <= 0:
        raise ValueError("scale must be positive.")
    return [low / scale, high / scale]
