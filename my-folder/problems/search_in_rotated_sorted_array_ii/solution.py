class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        return any(elem == target for elem in nums)