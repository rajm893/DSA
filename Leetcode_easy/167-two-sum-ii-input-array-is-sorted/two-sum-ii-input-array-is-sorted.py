class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        seen = {}
        for i in range(len(numbers)):
            second_num = target - numbers[i]
            if second_num in seen:
                return [seen[second_num]+1, i+1]
            seen[numbers[i]] = i


                