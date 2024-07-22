class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indeces = {}
        for i, elem in enumerate(nums):
            if (j := indeces.get(elem)) is not None and i - j <= k:
                return True
            indeces[elem] = i
        return False
