'''
2315. You are given a string s, where every two consecutive vertical bars '|' are 
grouped into a pair. In other words, the 1st and 2nd '|' make a pair, the 3rd and 4th
 '|' make a pair, and so forth.

Return the number of '*' in s, excluding the '*' between each pair of '|'.

Note that each '|' will belong to exactly one pair.

 

Example 1:

Input: s = "l|*e*et|c**o|*de|"
Output: 2
'''

class Solution:
    def countAsterisks(self, s: str) -> int:
        count = 0
        ans = 0
        for i in s:
            if i == '|':
                count += 1
            if count % 2 == 0:
                if i == '*':
                    ans += 1
        return ans