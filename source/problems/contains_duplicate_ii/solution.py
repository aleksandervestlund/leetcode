class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        indeces: dict[int, int] = {}
        for i, elem in enumerate(nums):
            if (j := indeces.get(elem)) is not None and i - j <= k:
                return True
            indeces[elem] = i
        return False
