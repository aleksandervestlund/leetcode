class Solution:
    def merge(
        self, nums1: list[int], m: int, nums2: list[int], n: int
    ) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2
        nums1.sort()
        # nums2.append(float("inf"))
        # nums3 = nums1[:m] + [float("inf")]
        # left = nums3.pop(0)
        # right = nums2.pop(0)

        # for k in range(m + n):
        #     if left <= right:
        #         nums1[k] = left
        #         left = nums3.pop(0)
        #     else:
        #         nums1[k] = right
        #         right = nums2.pop(0)
