class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        max_len = 1
        left = 0
        right = 1
        chars = {s[0]}

        while right < len(s):
            if (next_char := s[right]) in chars:
                chars.discard(s[left])
                left += 1
            else:
                chars.add(next_char)
                right += 1
                max_len = max(max_len, len(chars))

        return max_len
