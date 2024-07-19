class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = ""
        for chars in zip(*strs):
            chars = set(chars)
            if len(chars) != 1:
                break            
            pre += chars.pop()
        return pre