from re import fullmatch


class Solution:
    def isNumber(self, s: str) -> bool:
        pattern = "[+-]?((\d+(\.\d*)?)|(\.\d+))([eE][+-]?\d+)?"
        return fullmatch(pattern, s)