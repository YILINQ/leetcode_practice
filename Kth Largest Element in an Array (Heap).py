from heapq import *
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        for num in nums:
            heappush(heap, num)
        for i in range(len(nums) - k):
            heappop(heap)
        ans = heappop(heap)
        return ans