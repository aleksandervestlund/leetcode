class Solution:
    def searchInsert(self, nums: List[int], target: int, p: int = 0, r: Optional[int] = None) -> int:
        if r is None:
            r = len(nums) - 1
        if p > r:
            return p
        q = (p + r) // 2
        if target == nums[q]:
            return q
        if target < nums[q]:
            return self.searchInsert(nums, target, p, q - 1)
        return self.searchInsert(nums, target, q + 1, r)