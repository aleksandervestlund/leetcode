class Solution:
    def findMedianSortedArrays(
        self, nums1: list[int], nums2: list[int]
    ) -> float:
        n = sorted(nums1 + nums2)
        i = len(n) / 2

        if len(n) % 2:
            return n[int(i)]
        return (n[int(i)] + n[int(i) - 1]) / 2
