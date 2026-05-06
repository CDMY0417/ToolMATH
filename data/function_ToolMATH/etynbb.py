def tangent_periodic_equivalence(angle: int, period: int = 180) -> int:
    equivalent_angle = angle % period
    return equivalent_angle
