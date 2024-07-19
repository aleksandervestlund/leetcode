class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)[::-1]
        if x[-1] == "-":
            x = "-" + x[:-1]
        x = int(x)
        return x if x.bit_length() < 32 else 0
