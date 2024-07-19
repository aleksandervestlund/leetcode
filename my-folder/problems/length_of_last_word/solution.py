class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        for elem in reversed(s.rstrip(" ")):
            if elem == " ":
                return length
            length += 1
        return length