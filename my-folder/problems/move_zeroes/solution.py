class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i, elem in reversed(tuple(enumerate(nums))):
            if elem == 0:
                nums.append(nums.pop(i))
