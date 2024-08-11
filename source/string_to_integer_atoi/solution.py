class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip(" ")
        if not s:
            return 0
        sign = ""
        for char in s:
            if (not sign and char in {"+", "-"}) or char.isdigit():
                sign += char
            else:
                break
        if sign in {"+", "-", ""}:
            return 0
        signn = max(-(2**31), int(sign))
        return min(2**31 - 1, signn)
