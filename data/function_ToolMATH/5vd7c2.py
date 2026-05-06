def pairwise_differences(nums: list[int]) -> set:
    differences = set()
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            differences.add(abs(nums[i] - nums[j]))
    return differences
