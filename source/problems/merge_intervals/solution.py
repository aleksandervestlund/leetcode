class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        new_intervals = [intervals.pop(0)]
        while intervals:
            elem = intervals.pop(0)
            if elem[0] <= new_intervals[-1][1]:
                new_intervals[-1][1] = max(elem[1], new_intervals[-1][1])
            else:
                new_intervals.append(elem)
        return new_intervals
