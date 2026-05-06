def calculate_height_with_shadow_ratio(ref_height: float, ref_shadow: float, target_shadow: float) -> float:
    ratio = ref_height / ref_shadow
    target_height = ratio * target_shadow
    return target_height
