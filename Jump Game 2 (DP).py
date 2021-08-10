class Solution:
    def jump(self, nums) -> int:

        # typical LIS way to do this
        # a little bit slow
        f = []
        for i in range(len(nums)):
            f.append(0)

        f[0] = 0
        for i in range(1, len(nums)):
            min_step = len(nums)
            for j in range(i):
                if nums[j] >= i - j and f[j] + 1 < min_step:
                    min_step = f[j] + 1
            f[i] = min_step
        return f[-1]