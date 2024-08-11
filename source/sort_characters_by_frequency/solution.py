from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        return "".join(char * amount for char, amount in Counter(s).most_common())
