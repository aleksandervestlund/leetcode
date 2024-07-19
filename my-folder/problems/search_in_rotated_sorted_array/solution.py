class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i, elem in enumerate(nums):
            if elem == target:
                return i
        return -1
