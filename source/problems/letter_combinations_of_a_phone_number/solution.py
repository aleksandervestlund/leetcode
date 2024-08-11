from itertools import product


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        letters = {
            "2": {"a", "b", "c"},
            "3": {"d", "e", "f"},
            "4": {"g", "h", "i"},
            "5": {"j", "k", "l"},
            "6": {"m", "n", "o"},
            "7": {"p", "q", "r", "s"},
            "8": {"t", "u", "v"},
            "9": {"w", "x", "y", "z"},
        }
        return [
            "".join(elem)
            for elem in product(*(letters[digit] for digit in digits))
        ]
