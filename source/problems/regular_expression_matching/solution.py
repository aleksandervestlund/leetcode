from re import fullmatch


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return fullmatch(p.replace("***", "*"), s) is not None
