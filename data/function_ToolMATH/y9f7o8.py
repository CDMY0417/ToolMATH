def apply_linear_transformation(range_min: int, range_max: int, slope: int, intercept: int):
    transformed_min = slope * range_min + intercept
    transformed_max = slope * range_max + intercept
    return transformed_min, transformed_max
