class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        tot_string = s.split()
        return len(tot_string[-1])

