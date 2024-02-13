class Solution:
    def romanToInt(self, s: str) -> int:
        
        roman_to_int = {"I":1, "V":5, "X":10, "L":50,"C":100, "D":500, 
                        "M":1000}
        value = 0
        for i in range(len(s)):
            if i+1 < len(s) and roman_to_int[s[i]] < roman_to_int[s[i+1]]:
                value -= roman_to_int[s[i]]
            else:
                value += roman_to_int[s[i]]
        return value