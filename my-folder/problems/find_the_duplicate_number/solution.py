class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for elem in nums:
            if elem in seen:
                return elem
            seen.add(elem)
