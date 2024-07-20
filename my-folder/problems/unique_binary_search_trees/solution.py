from math import factorial


class Solution:
    def numTrees(self, n: int) -> int:
        return factorial(2 * n) // (factorial(n)**2 * (n + 1))