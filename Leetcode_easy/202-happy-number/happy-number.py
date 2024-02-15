class Solution:
    def isHappy(self, n: int) -> bool:

        visited = set()
        
        def sumOfSquares(n):
            res = 0    
            while n:
                num = n%10
                res += num**2
                n = n // 10
            return res

        while n not in visited:
            visited.add(n)
            n = sumOfSquares(n)
            if n == 1:
                return True
        return False
