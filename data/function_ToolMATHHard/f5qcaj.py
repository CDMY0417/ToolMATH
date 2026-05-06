def similar_triangles_height(shadow_unknown: float, known_height: float, known_shadow: float):
    """Return height from similar triangles."""
    if shadow_unknown <= 0 or known_height <= 0 or known_shadow <= 0:
        raise ValueError("Inputs must be positive.")
    return shadow_unknown * known_height / known_shadow
