class Solution:

    def reverse(self, nums, i, j):

        lt = i
        rt = j
        while lt < rt:
            tmp = nums[lt]
            nums[lt] = nums[rt]
            nums[rt] = tmp
            lt += 1
            rt -= 1


    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        self.reverse(nums, 0, len(nums)-k-1)
        self.reverse(nums, len(nums)-k, len(nums)-1)
        self.reverse(nums, 0, len(nums)-1)
        
      