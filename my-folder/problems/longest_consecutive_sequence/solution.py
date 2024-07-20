class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_length = 1
        curr_length = 0
        nums.sort()
        curr_val = nums[0] - 1
        for elem in nums:
            if elem == curr_val:
                continue
            if elem == curr_val + 1:
                curr_length += 1
            else:
                curr_length = 1
            max_length = max(max_length, curr_length)
            curr_val = elem
        return max_length