from itertools import chain, combinations


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        return [
            list(subset)
            for subset in chain.from_iterable(
                combinations(nums, r) for r in range(len(nums) + 1)
            )
        ]
