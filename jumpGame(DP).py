class Solution:
    def canJump(self, nums: List[int]) -> bool:
        f = [True]
        n = len(nums)
        for i in range(1, n):
            ans = any([nums[j] >= i - j and f[j] for j in range(i)])
            f.append(ans)
            #     if nums[j] >= i - j:
            #         f.append(True)
            #         break
            # f.append(False)
        print(f)
        return f[-1]