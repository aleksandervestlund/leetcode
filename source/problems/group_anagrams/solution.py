class Solution:
    @staticmethod
    def groupAnagrams(strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for elem in strs:
            key = "".join(sorted(elem))
            anagrams[key] = anagrams.get(key, []) + [elem]
        return list(anagrams.values())
