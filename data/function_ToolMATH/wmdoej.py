def angle_bisector_theorem_segment(a: int, c: int, bc: int) -> float:
    ratio_a_c = a / (a + c)
    segment_a = ratio_a_c * bc
    return segment_a
