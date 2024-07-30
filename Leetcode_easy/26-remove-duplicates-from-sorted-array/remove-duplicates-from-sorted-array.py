class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        arr = []
        k = 0
        for i in range(len(nums)):
            if nums[i] not in arr:
                nums[k] = nums[i]
                arr.append(nums[i])
                k += 1
        return k 
                
