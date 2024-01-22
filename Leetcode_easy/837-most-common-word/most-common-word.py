import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.findall(r'\w+', paragraph.lower())
        
        word_count = Counter(words)
        
        for word in banned:
            if word in word_count:
                del word_count[word]
        
        most_common_words = word_count.most_common()
        
        if most_common_words:
            return most_common_words[0][0]
        else:
            return ""
