class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:        
        for i, j in enumerate(nums):
            if target-j in nums[i+1:]:
                return [i, i+1+nums[i+1:].index(target-j)]