class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}        
        for i, num in enumerate(nums):
            
            ans = target - nums[i]
            if ans in seen:
                return [i, seen[ans]]
            seen[num] = i 
            