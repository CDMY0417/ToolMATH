def largest_and_smallest_sum(nums: list[int]):
    if not nums:
        return None
    return max(nums) + min(nums)
