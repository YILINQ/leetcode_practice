class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda s: (s[0], s[1]))
        result = []
        if intervals == []:
            return []
        current_interval = intervals[0]
        for i in range(1, len(intervals)):
            if current_interval[0] <= intervals[i][0] <= current_interval[1]:
                # overlapping
                current_interval[1] = max(current_interval[1], intervals[i][1])
            else:
                result.append(current_interval)
                current_interval = intervals[i]
        result.append(current_interval)
        return result