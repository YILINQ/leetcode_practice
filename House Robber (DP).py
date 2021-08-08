class Solution:
    def rob(self, nums) -> int:
        if not nums:
            return 0
        opt = [nums[0]]
        if len(nums) >= 2:
            opt.append(max(nums[0], nums[1]))
        if len(nums) > 2:
            for i in range(2, len(nums)):
                temp = max(opt[i-1], opt[i-2]+nums[i])
                opt.append(temp)
        return opt[-1]