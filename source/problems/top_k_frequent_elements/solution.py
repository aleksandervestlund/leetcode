from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [elem[0] for elem in Counter(nums).most_common(k)]
