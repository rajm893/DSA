class Solution:
    # Can also use while loop over here
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for j in range(len(t)):
            if i<len(s) and s[i] == t[j]:
                i += 1
        if i == len(s):
            return True
        return False