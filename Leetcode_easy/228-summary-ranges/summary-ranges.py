class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        start, end = nums[0], nums[0]
        res = []
        for i in range(1, len(nums)):
            if nums[i] > end+1:
                # start printing the range
                if start != end:
                    res.append(f"{start}->{end}")
                else:
                    res.append(f"{start}")
                start, end = nums[i], nums[i]
            else:
                end = nums[i]
        if start != end:
            res.append(f"{start}->{end}")
        else:
            res.append(f"{start}")
        return res

