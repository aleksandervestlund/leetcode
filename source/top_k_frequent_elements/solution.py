from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        return [elem[0] for elem in Counter(nums).most_common(k)]
