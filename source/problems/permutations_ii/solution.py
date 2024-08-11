from itertools import permutations


class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        return set(list(permutations(nums)))
