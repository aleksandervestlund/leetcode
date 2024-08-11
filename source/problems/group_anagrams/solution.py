from collections import defaultdict


class Solution:
    @staticmethod
    def groupAnagrams(strs: list[str]) -> list[list[str]]:
        anagrams = defaultdict(list)
        for elem in strs:
            key = "".join(sorted(elem))
            anagrams[key].append(elem)
        return list(anagrams.values())
