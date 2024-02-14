class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # we have to use 2 pointers to solve it linear time

        l = 0
        r = len(numbers)-1

        while l < r:
            curr = numbers[l] + numbers[r]
            if curr > target:
                r -= 1
            elif curr < target:
                l += 1
            else:
                return [l+1, r+1]