class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        k = len(needle)
        for i in range(len(haystack)):
            if haystack[i] == needle[0] and haystack[i:i+k] == needle:
                    return i
        return -1