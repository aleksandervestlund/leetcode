class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = ""
        maks = 0
        for i in s:
            if i not in sub:
                sub += i
                maks = max(maks, len(sub))
            else:
                sub = sub.split(i)[1] + i
        return maks
