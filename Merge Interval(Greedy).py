# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda x:x.start)
        result = []
        size = len(intervals)
        for i in range(size):
            if result == []:
                result.append(intervals[i])
            else:
                if result[-1].start <= intervals[i].start <= result[-1].end:
                    result[-1].end = max(intervals[i].end, result[-1].end)
                else:
                    result.append(intervals[i])
        return result