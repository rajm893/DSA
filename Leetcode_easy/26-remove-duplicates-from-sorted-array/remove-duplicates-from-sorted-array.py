class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        arr = []
        k = 0
        for i in range(len(nums)):  
            if nums[i] not in arr:
                arr.append(nums[i])
                nums[k] = nums[i]
                k += 1
        return k

                
