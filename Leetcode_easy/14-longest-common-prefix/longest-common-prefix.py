class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word = strs[0]
        res = ""
        for i in range(len(word)):
            for s in strs:
                if i == len(s) or s[i] != word[i]:
                    return res
            res += word[i]
        return res
