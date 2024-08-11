class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        return sum((ord(elem) - 64) * 26**i for i, elem in enumerate(reversed(columnTitle)))