class Solution:
    def intToRoman(self, num: int) -> str:
        symbols = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M",
        }
        leading = 10 ** len(str(num))
        s = ""

        while num:
            leading //= 10
            digit, num = divmod(num, leading)
            if digit in {4, 9}:
                s += symbols[leading] + symbols[(digit + 1) * leading]
                continue
            if digit > 4:
                s += symbols[5 * leading]
                digit -= 5
            if digit == 0:
                continue
            s += digit * symbols[leading]

        return s
