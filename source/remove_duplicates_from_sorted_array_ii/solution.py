class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        curr = nums[-1]
        curr_count = 0
        for i, elem in reversed(list(enumerate(nums))):
            if curr == elem:
                curr_count += 1
                if curr_count > 2:
                    nums.pop(i)
            else:
                curr = elem
                curr_count = 1
        return len(nums)
