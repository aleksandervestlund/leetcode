class Solution:
    def longestPalindrome(self, s: str) -> str:
        start_idx = 0
        end_idx = 1
        longest = ""
        current = ""

        while end_idx <= len(s):
            current = s[start_idx:end_idx]

            if current == current[::-1]:
                if len(longest) < end_idx - start_idx:
                    longest = current

                end_idx += 1
                start_idx = 0
            else:
                start_idx += 1
        
        return longest



