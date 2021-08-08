class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp_max = []
        dp_min = []
        for i in range(len(nums)):
            dp_max.append(0)
            dp_min.append(0)

        dp_max[0] = nums[0]
        dp_min[0] = nums[0]
        for i in range(1, len(nums)):
            dp_max[i] = max(dp_max[i - 1] * nums[i], nums[i], dp_min[i - 1] * nums[i])
            dp_min[i] = min(dp_max[i - 1] * nums[i], nums[i], dp_min[i - 1] * nums[i])
        print(dp_max)
        print(dp_min)
        return max(dp_max)