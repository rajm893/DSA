class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest, last, jump = 0,0,0
        for i in range(len(nums)-1):
            farthest = max(farthest, i + nums[i])        
            if i == last:
                jump += 1
                last = farthest
        return jump