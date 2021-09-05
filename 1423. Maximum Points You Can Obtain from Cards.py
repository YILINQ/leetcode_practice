class Solution:
    # TLE, so try another way round
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k == len(cardPoints):
            return sum(cardPoints)
        new_array = cardPoints.copy()
        new_array.extend(cardPoints[:k])
        n = len(cardPoints)
        max_sum = sum(cardPoints[:k])
        for i in range(n-k, n):
            if sum(new_array[i: i+k]) > max_sum:
                max_sum = sum(new_array[i: i+k])
        return max_sum


    # instead of summing every thing up, instead using a sliding window to subtrack the thing we dont need
    def maxScore_2(self, cardPoints: List[int], k: int) -> int:
        array_sum = sum(cardPoints)

        max_sum = sum(cardPoints[:k])
        n = len(cardPoints)
        for i in range(k):
            current_sum = array_sum - sum(cardPoints[i: i + n - k])
            if current_sum > max_sum:
                max_sum = current_sum
        return max_sum


    # still TLE, try prefix sum
    # keep left and right for each end
    # update k + 1 times, faster than 99%
    def maxScore_3(self, cardPoints: List[int], k: int) -> int:
        if k == len(cardPoints):
            return sum(cardPoints)

        # keep a left and a right sum
        max_sum = -1
        left = 0
        right = sum(cardPoints[-k:])
        for i in range(k + 1):
            if left + right > max_sum:
                max_sum = left + right
            left += cardPoints[i]
            right -= cardPoints[-k + i]
        return max_sum