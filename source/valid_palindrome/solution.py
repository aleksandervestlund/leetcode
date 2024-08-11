class Solution:
    def isPalindrome(self, s: str) -> bool:
        return (string := "".join(elem.lower() for elem in s if elem.isalnum())) == string[::-1]
