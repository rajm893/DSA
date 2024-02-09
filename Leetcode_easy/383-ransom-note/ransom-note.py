class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        magazine = list(magazine)
        for r in ransomNote:
            if r in magazine:
                magazine.remove(r)
            else:
                return False
        return True
        












        # magazine = list(magazine)
        # for i in ransomNote:
        #     if i in magazine:
        #         magazine.remove(i)
        #     else:
        #         return False
        # return True