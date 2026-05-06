import math

def unit_vector_from_points(px: float, py: float, qx: float, qy: float):
    """Return unit vector components [ux,uy] from P to Q."""
    dx = qx - px
    dy = qy - py
    norm = math.hypot(dx, dy)
    if norm == 0:
        raise ValueError("Points must be distinct.")
    return [dx / norm, dy / norm]
