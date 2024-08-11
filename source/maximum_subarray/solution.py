class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maks = nums[0]
        total = 0

        for tall in nums:
            total = max(0, total)
            total += tall
            maks = max(maks, total)
        return maks
