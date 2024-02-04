class Solution:
    def checkString(self, s: str) -> bool:
        sort = "".join(sorted(s))
        if s == sort:
            return True
        else:
            return False
