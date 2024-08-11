from itertools import permutations


class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        return [list(perm) for perm in set(permutations(nums))]
