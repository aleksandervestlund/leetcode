class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        seen = set()
        indeces = []
        amount = 0
        for i, elem in enumerate(nums):
            if elem in seen:
                indeces.append(i)
            else:
                seen.add(elem)
        for idx in reversed(indeces):
            nums.pop(idx)
        return len(seen)
