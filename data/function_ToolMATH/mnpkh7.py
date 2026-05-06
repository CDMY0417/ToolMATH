def compute_remainder_product_modulo(nums: list[int], mod: int) -> int:
    product = 1
    for num in nums:
        product *= num
    return product % mod
