class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        DupIdxMap = {}
        for i, num in enumerate(nums):
            if num in DupIdxMap and abs(i - DupIdxMap[num]) <= k:
                return True
            DupIdxMap[num] = i
        return False