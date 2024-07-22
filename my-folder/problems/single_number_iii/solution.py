class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        return [elem[0] for elem in Counter(nums).most_common()[-2:]]
