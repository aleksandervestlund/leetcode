class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        return [
            key
            for key, value in Counter(
                s[i : i + 10] for i in range(len(s) - 9)
            ).items()
            if value > 1
        ]
