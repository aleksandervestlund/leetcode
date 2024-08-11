class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        pre = ""
        for chars in zip(*strs):
            charss = set(chars)
            if len(chars) != 1:
                break
            pre += charss.pop()
        return pre
