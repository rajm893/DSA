class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            word = list(word)
            if word == word[::-1]:
                return "".join(word)
        return ""
        