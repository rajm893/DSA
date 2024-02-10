class Solution:
    def trap(self, height: List[int]) -> int:
        
        leftArray = [0]*len(height)
        rightArray = [0]*len(height)
        trap_value = 0
        leftArray[0]   = height[0]
        rightArray[-1] = height[-1]

        for i in range(1, len(leftArray)):
            leftArray[i] = max(height[i], leftArray[i-1])

        for j in range(len(rightArray)-2, -1, -1):
            rightArray[j] = max(height[j], rightArray[j+1])

        for k in range(len(height)):
            trap_value += min(leftArray[k], rightArray[k]) - height[k]

        return trap_value
