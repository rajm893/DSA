class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        nums.sort()
        total = 0
        res = -1
        for num in nums:
            if total > num:
                res = total+num
            total += num
        return res