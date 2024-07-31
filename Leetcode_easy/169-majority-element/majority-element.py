class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        maj = len(nums) // 2
        unique_nums = set(nums)
        for i in unique_nums:
            if nums.count(i) > maj:
                return i
