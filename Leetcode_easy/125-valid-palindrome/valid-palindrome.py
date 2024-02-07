class Solution:
    def isPalindrome(self, s: str) -> bool:
        c_str = ''
        for char in s:
            if char.isalnum():
                c_str += char.lower()
        return c_str == c_str[::-1]
