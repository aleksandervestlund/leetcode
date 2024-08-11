from collections import Counter
from itertools import takewhile


class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        k = len(nums) // 3
        return [
            elem[0]
            for elem in takewhile(
                lambda x: x[1] > k, Counter(nums).most_common()
            )
        ]
