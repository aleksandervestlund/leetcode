from collections import defaultdict


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numbers = defaultdict(list)

        for i, el in enumerate(nums):
            numbers[el].append(i)

        for i, elem in numbers.items():
            if 2 * i == target:
                if len(elem) > 1:
                    return elem[:2]
            elif (other := numbers.get(target - i)) is not None:
                return [elem[0]] + [other[0]]

        return []
