from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        dict_t: dict[str, int] = defaultdict(int)
        for char in t:
            dict_t[char] += 1
        required = len(dict_t)
        l = 0
        r = 0
        formed = 0
        window_counts: dict[str, int] = defaultdict(int)
        min_length = float("inf")
        min_window = ""
        while r < len(s):
            char = s[r]
            window_counts[char] += 1
            if char in dict_t and window_counts[char] == dict_t[char]:
                formed += 1
            while l <= r and formed == required:
                char = s[l]
                if r - l + 1 < min_length:
                    min_length = r - l + 1
                    min_window = s[l : r + 1]
                window_counts[char] -= 1
                if char in dict_t and window_counts[char] < dict_t[char]:
                    formed -= 1
                l += 1
            r += 1
        return min_window
