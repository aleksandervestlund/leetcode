class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def bisect(a: list[int], p: int, r: int, v: int) -> int:
            if p > r:
                return -1
            q = (p + r) // 2
            if v == a[q]:
                return q
            if v < a[q]:
                return bisect(a, p, q - 1, v)
            return bisect(a, q + 1, r, v)

        n = len(nums)
        idx = [bisect(nums, 0, n - 1, target)] * 2
        while idx[0] > 0 and nums[idx[0] - 1] == target:
            idx[0] -= 1
        while idx[1] < n - 1 and nums[idx[1] + 1] == target:
            idx[1] += 1
        return idx
