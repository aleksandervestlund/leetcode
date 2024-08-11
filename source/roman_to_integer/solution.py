class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        total = 0
        idx = 0

        while idx < len(s):
            sub = symbols.get(s[idx : idx + 2])
            if sub is not None:
                total += sub
                idx += 2
            else:
                total += symbols[s[idx]]
                idx += 1

        return total
