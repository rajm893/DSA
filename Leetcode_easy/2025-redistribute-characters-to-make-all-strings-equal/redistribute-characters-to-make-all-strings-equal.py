class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        
        complete_string  = "".join(words)
        k =  list(set(complete_string))
        for i in k:
            if complete_string.count(i) % len(words) != 0:
                return False
        return True
          

