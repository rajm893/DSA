class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False

        char_to_word_map = {}
        word_to_char_map = {}
        
        for c, w in zip(pattern, words):
            if c in char_to_word_map and char_to_word_map[c] != w:
                return False
            if w in word_to_char_map and word_to_char_map[w] != c:
                return False
            char_to_word_map[c] = w
            word_to_char_map[w] = c
        return True       