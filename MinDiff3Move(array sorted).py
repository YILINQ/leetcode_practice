class Solution:
    def minDifference(self, nums):
        if len(nums) <= 4:
            return 0
        n = len(nums)
        nums.sort()
        return min(nums[n - 4] - nums[0], nums[n - 3] - nums[1],
                   nums[n - 2] - nums[2], nums[n - 1] - nums[3])

