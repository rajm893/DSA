

'''

Find two distinct numbers in an array that add up to a given target.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


'''

def twosum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        ans = target - nums[i]
        if ans in seen:
            return [i, seen[ans]]
        seen[num] = i
    return seen

if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    seen = twosum(nums, target)
    print(seen)