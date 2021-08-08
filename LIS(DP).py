class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        ans = 1
        f = []
        for i in range(len(nums)):
            f.append(1)
        for i in range(len(nums)):
            temp = [1]
            for j in range(i):
                if (nums[i] > nums[j]):
                    temp.append(f[j] + 1)
                else:
                    temp.append(f[i])

            f[i] = max(temp)
        return max(f)