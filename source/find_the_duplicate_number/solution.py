class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        seen = set()
        for elem in nums:
            if elem in seen:
                return elem
            seen.add(elem)
        return float("-inf")  # type: ignore
