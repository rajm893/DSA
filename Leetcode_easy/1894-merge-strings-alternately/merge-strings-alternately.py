class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        word1 = list(word1)
        word2 = list(word2)
        max_len = max(len(word1),len(word2))
        for i in range(max_len):
            if i < len(word1):
                res.append(word1[i])
            if i < len(word2):
                res.append(word2[i])
        return "".join(res)

        