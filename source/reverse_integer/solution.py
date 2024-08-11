class Solution:
    def reverse(self, x: int) -> int:
        xx = str(x)[::-1]
        if xx[-1] == "-":
            xx = "-" + xx[:-1]
        x = int(xx)
        return x if x.bit_length() < 32 else 0
