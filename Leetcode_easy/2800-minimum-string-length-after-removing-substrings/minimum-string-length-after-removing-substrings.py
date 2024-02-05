class Solution:
    def minLength(self, s: str) -> int:
        while True:
            isAB = False
            isCD = False
            if "AB" in s:
                isAB = True
                s = s.replace("AB","")
            if "CD" in s:
                isCD = True
                s = s.replace("CD","")
            if not isAB and not isCD:
                return len(s) 