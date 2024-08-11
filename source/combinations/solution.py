from itertools import combinations


class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        return [list(elem) for elem in combinations(range(1, n + 1), k)]
