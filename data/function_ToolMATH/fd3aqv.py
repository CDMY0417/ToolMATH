def sqrt_of_product(nums: list[float]) -> float:
    import math
    product = 1
    for num in nums:
        product *= num
    return math.sqrt(product)
