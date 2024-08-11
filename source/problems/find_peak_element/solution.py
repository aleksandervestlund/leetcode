class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        nums.insert(0, float("-inf"))  # type: ignore
        nums.append(float("-inf"))  # type: ignore
        for i in range(1, len(nums) - 1):
            if nums[i - 1] < nums[i] > nums[i + 1]:
                return i - 1
        return -1
