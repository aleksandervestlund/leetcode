from collections import Counter


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        return Counter(nums).most_common()[-1][0]
