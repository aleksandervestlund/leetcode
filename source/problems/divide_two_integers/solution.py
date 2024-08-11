class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        return max(min(int(dividend / divisor), 2**31 - 1), -2**31)
