class Solution:
    def sortColors(self, nums: List[int]) -> None:
        b = nums.copy()
        k = max(nums)
        n = len(nums)
        c = [0] * (k + 1)

        for i in range(n):
            c[b[i]] += 1

        for i in range(1, k + 1):
            c[i] += c[i - 1]

        for i in range(n - 1, -1, -1):
            nums[c[b[i]] - 1] = b[i]
            c[b[i]] -= 1
        