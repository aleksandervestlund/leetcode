class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(1, len(triangle)):
            prev = triangle[i - 1]
            curr = triangle[i]
            curr[0] += prev[0]
            curr[-1] += prev[-1]
            for j in range(1, len(curr) - 1):
                left = prev[j - 1]
                right = prev[j]
                curr[j] += min(left, right)
        return min(triangle[-1])
