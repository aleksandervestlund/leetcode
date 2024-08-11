class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        return any(elem == target for elem in nums)
