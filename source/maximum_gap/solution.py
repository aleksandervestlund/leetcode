class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        nums = sorted(set(nums))
        n = len(nums)
        if n < 2:
            return 0
        return max(nums[i + 1] - nums[i] for i in range(n - 1))
