class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        ranges = [[nums.pop(0)]]

        for elem in nums:
            if elem == ranges[-1][-1] + 1:
                ranges[-1].append(elem)
            else:
                ranges.append([elem])

        return [
            f"{elem[0]}{'' if len(elem) == 1 else f'->{elem[-1]}'}"
            for elem in ranges
        ]
