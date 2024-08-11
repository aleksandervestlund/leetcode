class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        indeces = []
        for i, elem in enumerate(nums):
            if elem == val:
                indeces.append(i)
        for idx in reversed(indeces):
            nums.pop(idx)
        return len(nums)
