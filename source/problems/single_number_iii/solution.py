class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        return [elem[0] for elem in Counter(nums).most_common()[-2:]]
