class Solution:
    def isPalindrome(self, x: int) -> bool:
        return (s := str(x)) == s[::-1]