class Solution:
    import math
    def sumUp(self, k, piles):
        result = 0
        for num in piles:
            if k != 0:
                if num < k:
                    result +=1
                else:
                    result += math.ceil(num / k)
        return result
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)
        if sum(piles) <= h:
            return 1
        # binary search on region where k could be
        l = 0
        r = max(piles)
        while l < r:
            mid = (l + r) // 2
            if self.sumUp(mid, piles) <= h:
                r = mid
            else:
                l = mid + 1
        return l