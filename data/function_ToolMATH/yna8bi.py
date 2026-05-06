def product_of_numbers_f(nums: list[float]) -> float:
    product = 1
    for num in nums:
        product *= num
    return product
