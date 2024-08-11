from math import prod


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        zeroes = nums.count(0)

        if zeroes > 1:
            return [0] * n

        product = prod(elem for elem in nums if elem != 0)

        if zeroes == 1:
            return [0 if elem else product for elem in nums]
        return [product // nums[i] for i in range(n)]
