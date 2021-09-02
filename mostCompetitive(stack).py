class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            while result != [] and result[-1] > nums[i] and len(result) + len(nums) - i - 1 >= k:
                result.pop()
            result.append(nums[i])
        return result[:k]